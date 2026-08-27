# Maintainer: Andres Rodriguez <andresx7@gmail.com>

# The dock updater code is proprietary, which means that in this
# PKGBUILD we only have access to prebuilt binaries.

pkgname=jupiter-dock-updater-bin
_srctag=jupiter-20260811.01
_srcver=${_srctag#jupiter-}
pkgver=${_srcver//-/.}
pkgrel=1
pkgdesc="Firmware updater for the Steam Deck Dock"
url="https://gitlab.steamos.cloud/jupiter/jupiter-dock-updater-bin"
arch=(x86_64)
license=(proprietary)
depends=()
makedepends=(git openssh)
source=("git+ssh://git@gitlab.steamos.cloud/jupiter/jupiter-dock-updater-bin.git#tag=$_srctag")
sha256sums=('eca9ffbe405c7ee448a623c8843edb6479761d9af77619f63440bf4d7dd171c6')

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
