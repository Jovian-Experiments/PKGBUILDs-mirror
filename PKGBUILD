# Maintainer: Antonio Rojas <arojas@archlinux.org>

pkgname=plasma-remotecontrollers
pkgver=5.26.90.r256.g8daeecc
# _dirver=$(echo $pkgver | cut -d. -f1-3)
pkgrel=1
pkgdesc='Translate various input device events into keyboard and pointer events'
arch=(x86_64)
url='https://plasma-bigscreen.org/'
license=(GPL2)
depends=(plasma-workspace)
makedepends=(extra-cmake-modules plasma-wayland-protocols libcec)
optdepends=('libcec: TV remotes support')

# There is no Qt6 release of plasma-remotecontrollers at present, take master at the time of 6.2
_commit=8daeecc2de0a10cfaca3638d68e5b2b2c5921413

source=(${pkgname}::git+https://invent.kde.org/plasma-bigscreen/plasma-remotecontrollers.git#commit=${_commit}
        CMakeLists.txt.patch  # Disable installing the autostart entry
        plasma-remotecontrollersrc.patch  # Patch some defaults, including OSD name, some bindings, and disable evdev
        systemd.service
        udev.rules)
sha256sums=('SKIP'
            '17a81c30760b6fd297935ca5b633abbd2b13e2f24e5c26b660c8ee9ca37ed29f'
            'fb7686b04d351edcb9e632def80d220f7c0186a2558d9cdfd68875a08579bd5f'
            '0e05ea16cd8541bde1a33c23574d111a27965058a01c0730595eb0cd31cd655d'
            'd4dc16146515250a5a6f6d4a3b02ff05d5890474f27b1ee59cee5fa7b230d0e0')
validpgpkeys=('E0A3EB202F8E57528E13E72FD7574483BB57B18D'  # Jonathan Esk-Riddell <jr@jriddell.org>
              '0AAC775BB6437A8D9AF7A3ACFE0784117FBCE11D'  # Bhushan Shah <bshah@kde.org>
              'D07BD8662C56CB291B316EB2F5675605C74E02CF'  # David Edmundson <davidedmundson@kde.org>
              '1FA881591C26B276D7A5518EEAAF29B42A678C20') # Marco Martin <notmart@gmail.com>

pkgver() {
  cd ${pkgname}
  git describe --long --abbrev=7 | sed 's/\([^-]*-g\)/r\1/;s/-/./g' | sed 's/^v//'
}

prepare() {
  cd "$srcdir"
  for PATCH in $(ls *.patch); do
    patch -d $pkgname -p1 < "$PATCH"
  done
}

build() {
  cmake -B build -S $pkgname \
    -DBUILD_TESTING=OFF
  cmake --build build
}

package() {
  DESTDIR="$pkgdir" cmake --install build
  install -Dm644 systemd.service "$pkgdir/usr/lib/systemd/user/plasma-remotecontrollers.service"
  install -Dm644 udev.rules "$pkgdir/usr/lib/udev/rules.d/70-plasma-remotecontrollers.rules"
  mkdir -p "$pkgdir/usr/lib/systemd/user/dev-cec0.device.wants"
  ln -s ../plasma-remotecontrollers.service "$pkgdir/usr/lib/systemd/user/dev-cec0.device.wants/"
  mkdir -p "$pkgdir/usr/lib/systemd/user/gamescope-session.service.wants"
  ln -s ../plasma-remotecontrollers.service "$pkgdir/usr/lib/systemd/user/gamescope-session.service.wants/"
}
