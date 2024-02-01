# Author : Vivek Das Mohapatra <vivek@collabora.com>

pkgname=('steamos-reset' 'steamos-reset-ui')
_srctag=jupiter-20240125.1
pkgver=${_srctag#jupiter-}
pkgrel=1
arch=('x86_64')
license=('GPL')
makedepends=('git' 'qt5-base' 'qt5-quickcontrols2')
depends=(curl bash steamos-efi steamos-atomupd-client-git jq)
url='https://gitlab.steamos.cloud/holo/steamos-reset'
source=("${pkgname}::git+${url}#tag=${_srctag}")
sha256sums=('SKIP')

build () {
    local unsplit=$(readlink -f .inst)
    cd "${pkgname}"
    autoreconf -ivf
    ./configure --prefix=/usr --libexecdir=/usr/lib --sbindir=/usr/bin \
                --with-ui=qml
    make && make DESTDIR=$unsplit install
}

_split_install ()
{
    local pkg=$1
    local from=$2
    local to=$3
    local src dir dst x

    local -a uifiles=(\
        /usr/share/steamos-reset/lighttpd/steamos-reset.conf \
        /usr/lib/steamos-reset/bin/steamos-reset-qml \
        /usr/bin/steamos-reset-service \
        /usr/share/applications/steamos-factory-reset.qml.desktop \
        /usr/share/steamos-reset/steamos-reset.svg \
        /usr/lib/systemd/system/steamos-reset.service)
    local -A UIFILES=()
    for x in "${uifiles[@]}"; do UIFILES["$x"]=1; done

    while read src
    do
        src=${src#.}
        case $pkg in
            steamos-reset)
                if [ ${UIFILES["$src"]:-0} -eq 1 ]; then continue; fi
                ;;
            steamos-reset-ui)
                if [ ${UIFILES["$src"]:-0} -ne 1 ]; then continue; fi
                ;;
        esac
        dst=${to}$(dirname $src)
        install -m755 -d $dst
        mv ${from}${src} $dst
    done < <(cd $from && find -mindepth 1 -type f)
}

package_steamos-reset() {
    local unsplit=$(readlink -f .inst)
    pkgdesc='Backend and CLI to reset SteamOS to a freshly installed state'

    _split_install "$pkgname" "$unsplit" "$pkgdir"
}

package_steamos-reset-ui() {
    local unsplit=$(readlink -f .inst)
    depends=(steamos-reset lighttpd gcc-libs qt5-base qt5-declarative)
    pkgdesc='GUI tool reset SteamOS to a freshly installed state'

    _split_install "$pkgname" "$unsplit" "$pkgdir"
}
