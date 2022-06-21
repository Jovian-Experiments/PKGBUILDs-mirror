# Maintainer: Andres Rodriguez <andresx7@gmail.com>

# The dock updater code is proprietary, which means that in this
# PKGBUILD we only have access to prebuilt binaries.

pkgname=jupiter-dock-updater-bin
_srctag=jupiter-20220615.02
_srcver=${_srctag#jupiter-}
pkgver=${_srcver//-/.}
pkgrel=1
pkgdesc="Firmware updater for the Steam Deck Dock"
url="https://gitlab.steamos.cloud/jupiter/jupiter-dock-updater-bin"
arch=(x86_64)
license=(proprietary)
depends=()
makedepends=(git)
source=("git+ssh://git@gitlab.steamos.cloud/jupiter/jupiter-dock-updater-bin.git#tag=$_srctag")
sha256sums=('SKIP')

prepare() {
    cd "$pkgname"
    # Nothing to do
}

build() {
    cd "$pkgname"
    # Nothing to do
}

package() {
    cd "$pkgname"
    cp -a "packaged/." "$pkgdir"
}
