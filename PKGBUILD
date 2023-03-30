# Maintainer: Antonio Rojas <arojas@archlinux.org>

pkgname=plasma-remotecontrollers
pkgver=5.27.3
pkgrel=1.1
pkgdesc='Translate various input device events into keyboard and pointer events'
arch=(x86_64)
url='https://plasma-bigscreen.org/'
license=(GPL2)
depends=(plasma-workspace)
makedepends=(extra-cmake-modules plasma-wayland-protocols libcec)
optdepends=('libcec: TV remotes support')
source=(https://download.kde.org/stable/plasma/$pkgver/$pkgname-$pkgver.tar.xz{,.sig}
        plasma-remotecontrollersrc.patch  # Patch the default config file to set the OSD name to "Steam Deck"
        CMakeLists.txt.patch  # Disable installing the autostart entry
        systemd.service
        udev.rules)
sha256sums=('3ce4c841fb538c012618f120922cb6595060a4208a0516bd41532004a12e5511'
            'SKIP'
            'b844b24d1364632c874ec27b69fe1294d6dbdf778e9af4de90da93245edb0b42'
            '17a81c30760b6fd297935ca5b633abbd2b13e2f24e5c26b660c8ee9ca37ed29f'
            '963a23f6f362845a11ec2f4dd1b19c321837cce1a3c8fccd0c452bac2dcc8e0a'
            'd4dc16146515250a5a6f6d4a3b02ff05d5890474f27b1ee59cee5fa7b230d0e0')
validpgpkeys=('E0A3EB202F8E57528E13E72FD7574483BB57B18D'  # Jonathan Esk-Riddell <jr@jriddell.org>
              '0AAC775BB6437A8D9AF7A3ACFE0784117FBCE11D'  # Bhushan Shah <bshah@kde.org>
              'D07BD8662C56CB291B316EB2F5675605C74E02CF'  # David Edmundson <davidedmundson@kde.org>
              '1FA881591C26B276D7A5518EEAAF29B42A678C20') # Marco Martin <notmart@gmail.com>

prepare() {
  cd "$srcdir"
  patch -d $pkgname-$pkgver -p1 < plasma-remotecontrollersrc.patch
  patch -d $pkgname-$pkgver -p1 < CMakeLists.txt.patch
}

build() {
  cmake -B build -S $pkgname-$pkgver \
    -DBUILD_TESTING=OFF
  cmake --build build
}

package() {
  DESTDIR="$pkgdir" cmake --install build
  install -Dm644 systemd.service "$pkgdir/usr/lib/systemd/user/plasma-remotecontrollers.service"
  install -Dm644 udev.rules "$pkgdir/usr/lib/udev/rules.d/70-plasma-remotecontrollers.rules"
}
