pkgname=steam-im-modules
_srctag=jupiter-20240131
pkgver=${_srctag//-/.}
pkgrel=1
pkgdesc="Steam Qt Keyboard Plug-in"
arch=(x86_64 i686 arm armv6h armv7h aarch64)
url="https://github.com/valve-project/steam-qt-keyboard-plugin"
license=(GPL3)
makedepends=('git' 'extra-cmake-modules' 'qt5-base' 'gtk3' 'gtk4')
optdepends=('qt5-base' 'gtk3' 'gtk4')
provides=(steam-im-modules)
conflicts=(steam-im-modules)
source=("$pkgname::git+${url}.git#tag=${_srctag}")
sha256sums=('SKIP')

build() {
  cmake -DCMAKE_INSTALL_PREFIX=/usr -DCMAKE_BUILD_TYPE=RelWithDebInfo -B build -S "${pkgname%-git}"
  cmake --build build --config RelWithDebInfo
}

package() {
  DESTDIR="${pkgdir}" cmake --install build --config RelWithDebInfo
}
