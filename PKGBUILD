# Maintainer: Felix Yan <felixonmars@archlinux.org>
# Maintainer: Antonio Rojas <arojas@archlinux.org>
# Contributor: Andrea Scarpino <andrea@archlinux.org>

# KWin is included in holo unpatched as it needs building against holo's libwayland

pkgname=kwin
pkgver=5.27.10
_dirver=$(echo $pkgver | cut -d. -f1-3)
pkgrel=4
pkgdesc='An easy to use, but flexible, composited Window Manager'
arch=(x86_64)
url='https://kde.org/plasma-desktop/'
license=(LGPL)
depends=(kscreenlocker xcb-util-cursor plasma-framework5 kcmutils5 breeze
         pipewire-session-manager libqaccessibilityclient lcms2 libxcvt "wayland>=1.23.0")
makedepends=(extra-cmake-modules qt5-tools kdoctools5 krunner5 wayland-protocols plasma-wayland-protocols python)
optdepends=('maliit-keyboard: virtual keyboard for kwin-wayland')
replaces=(kwayland-server)
groups=(plasma)
source=(https://download.kde.org/stable/plasma/$_dirver/$pkgname-$pkgver.tar.xz{,.sig})
install=$pkgname.install
sha256sums=('b85a25125900b62cb5a3c609961088c45a58f55004317e4f5e8ba2039ae6dac6'
            'SKIP')
validpgpkeys=('E0A3EB202F8E57528E13E72FD7574483BB57B18D'  # Jonathan Esk-Riddell <jr@jriddell.org>
              '0AAC775BB6437A8D9AF7A3ACFE0784117FBCE11D'  # Bhushan Shah <bshah@kde.org>
              'D07BD8662C56CB291B316EB2F5675605C74E02CF'  # David Edmundson <davidedmundson@kde.org>
              '1FA881591C26B276D7A5518EEAAF29B42A678C20') # Marco Martin <notmart@gmail.com>

build() {
  cmake -B build -S $pkgname-$pkgver \
    -DCMAKE_INSTALL_LIBEXECDIR=lib \
    -DBUILD_TESTING=OFF
  cmake --build build
}

package() {
  DESTDIR="$pkgdir" cmake --install build
}
