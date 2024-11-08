# Maintainer: Peter Jung <ptr1337@archlinux.org>
# Contributor: Denis Benato <benato.denis96@gmail.com>
# Contributor: William Edwards <shadowapex@gmail.com>

pkgname=inputplumber
pkgver=0.36.5
pkgrel=1
pkgdesc="Open source input router and remapper daemon for Linux"
arch=('x86_64')
options=(!lto)
url="https://github.com/ShadowBlip/InputPlumber"
license=('GPL-3.0-only')
depends=(
  dbus
  gcc-libs
  glibc
  libevdev
  libiio
  systemd-libs
)
makedepends=(
  clang
  cmake
  git
  make
  rust
)
source=("git+https://github.com/ShadowBlip/InputPlumber.git#tag=v${pkgver}")
sha256sums=('SKIP')

build() {
  cd "$srcdir/InputPlumber"
  make build
}

package() {
  cd "$srcdir/InputPlumber"
  make install PREFIX=${pkgdir}/usr NO_RELOAD=true
}
