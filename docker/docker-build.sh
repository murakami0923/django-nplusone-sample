#!/bin/bash

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

    IMG_BASE=django-docker
    current_dir=`pwd`/

    # ================================================================================
    # django-docker-lb-nginx : LB機能のnginx
    # ================================================================================
    dir=lb-nginx
    IMG=${IMG_BASE}-${env_name}-${dir}
    cd ${current_dir}/${dir}/
    
    echo docker build ${IMG}:${1}
    docker build ${opt} -t ${IMG}:${1} .

    if [ ${1} != "latest" ]; then
        echo "tagに「latest」以外のものが指定されたので、latestにタグ付けします。"
        docker tag ${IMG}:${1} ${IMG}:latest
    fi

    cd ${current_dir}/

    # ================================================================================
    # django-docker-app : アプリケーションサーバ
    # ================================================================================
    dir=app
    IMG=${IMG_BASE}-${env_name}-${dir}
    cd ${current_dir}/${dir}/
    
    echo docker build ${IMG}:${1}
    docker build ${opt} -t ${IMG}:${1} .

    if [ ${1} != "latest" ]; then
        echo "tagに「latest」以外のものが指定されたので、latestにタグ付けします。"
        docker tag ${IMG}:${1} ${IMG}:latest
    fi

    cd ${current_dir}/
}

# 引数別の処理定義
tag="latest"
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
