#!/bin/bash

source ./env.sh

function usage() {
  cat <<EOM
Usage: $(basename "$0") [OPTION]...
  -h          ヘルプを表示
  -n          キャッシュを使わない
  -t {tag名} : imageをビルドする際のタグ名（指定しない場合はlatestでビルドする）
  -e {環境名} : 環境名（develop / production）
EOM

  exit 2
}

function docker_build() {
    # ================================================================================
    # Docker Build (Product)
    # 1 : "tag": イメージのtag
    # 2 : "cache": キャッシュを使うかどうか（yes / no）
    # ================================================================================
    opt=""

    if [ ${2} == "no" ]; then
        opt="${opt} --no-cache"
    fi

    env_name=${3}
    if [ ${3} == "NO_ENV" ]; then
        env_name="develop"
    fi

    echo "env_name : ${env_name}"

    IMG_BASE=django-docker-nplus-sample
    current_dir=`pwd`/

    # ================================================================================
    # django-docker-app : アプリケーションサーバ
    # ================================================================================
    dir=app
    IMG=${IMG_BASE}-${env_name}-${dir}

    /bin/cp -Ra ./app/requirements/ ./docker/${dir}/

    cd ${current_dir}/docker/${dir}/

    echo docker build ${IMG}:${1}
    docker build \
        ${opt} \
        --build-arg ENV=${ENV}\
        --build-arg ENV_APP_GID=${ENV_APP_GID}\
        --build-arg ENV_APP_GNAME=${ENV_APP_GNAME} \
        --build-arg ENV_APP_UID=${ENV_APP_UID} \
        --build-arg ENV_APP_UNAME=${ENV_APP_UNAME} \
        -t ${IMG}:${1}\
        .

    cd ${current_dir}/

    rm -Rf ${current_dir}/docker/${dir}/requirements/
}

# 引数別の処理定義
tag="20220806"
cache="yes"
env="NO_ENV"

while getopts "he:t:n" optKey; do
    case "$optKey" in
        h|'--help')
            usage
            ;;
        e)
            echo "envが指定されました。"
            env=${OPTARG}
            ;;
        t)
            echo "tagが指定されました。"
            tag=${OPTARG}
            ;;
        n)
            cache="no"
            echo "キャッシュを使わないよう指定されました。"
            ;;
        *)
            usage
            ;;
    esac
done

echo "tag : ${tag}"
echo "cache : ${cache}"
echo "env : ${env}"

docker_build $tag $cache $env

# echo '----- docker build -----'
# docker_build
