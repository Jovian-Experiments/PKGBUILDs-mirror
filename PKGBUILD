# Maintainer: Antonio Rojas <arojas@archlinux.org>

pkgname=plasma-remotecontrollers
pkgver=5.27.11
_dirver=$(echo $pkgver | cut -d. -f1-3)
pkgrel=1.2
pkgdesc='Translate various input device events into keyboard and pointer events'
arch=(x86_64)
url='https://plasma-bigscreen.org/'
license=(GPL2)
depends=(plasma-workspace)
makedepends=(extra-cmake-modules plasma-wayland-protocols libcec)
optdepends=('libcec: TV remotes support')
source=(https://download.kde.org/stable/plasma/$_dirver/$pkgname-$pkgver.tar.xz{,.sig}
        0001-Allow-CEC-translated-key-events-to-be-rebound.patch
        0002-Add-a-signal-for-CEC-being-told-to-enter-standby.patch
        0003-Add-a-signal-for-CEC-being-made-the-active-source.patch
        0004-Allow-individual-backends-to-be-disabled-in-config.patch
        CMakeLists.txt.patch  # Disable installing the autostart entry
        plasma-remotecontrollersrc.patch  # Patch some defaults, including OSD name, some bindings, and disable evdev
        systemd.service
        udev.rules)
sha256sums=('59f37c7833797876ead26383077a08c7804bbf2c5208bdecd788a476045ce770'
            'SKIP'
            '1a4548b4b046e33a56ecb27fae2adee3008c51a757c28d2ec9bf55034bbdf664'
            'da75ca0a381ba9bb97c3dd5ad3a56b4f622e0df733c0237f12e150091f105b1e'
            '208b7640475a0f7647e0952061a9176fed7a3fd4ce9bfd8a087d03ed97bf1f70'
            '6adaf955fb93ebf378ad2b2ce54c50b68d19595642343c05135fc2fabf3881df'
            '17a81c30760b6fd297935ca5b633abbd2b13e2f24e5c26b660c8ee9ca37ed29f'
            'fb7686b04d351edcb9e632def80d220f7c0186a2558d9cdfd68875a08579bd5f'
            '0e05ea16cd8541bde1a33c23574d111a27965058a01c0730595eb0cd31cd655d'
            'd4dc16146515250a5a6f6d4a3b02ff05d5890474f27b1ee59cee5fa7b230d0e0')
validpgpkeys=('E0A3EB202F8E57528E13E72FD7574483BB57B18D'  # Jonathan Esk-Riddell <jr@jriddell.org>
              '0AAC775BB6437A8D9AF7A3ACFE0784117FBCE11D'  # Bhushan Shah <bshah@kde.org>
              'D07BD8662C56CB291B316EB2F5675605C74E02CF'  # David Edmundson <davidedmundson@kde.org>
              '1FA881591C26B276D7A5518EEAAF29B42A678C20') # Marco Martin <notmart@gmail.com>

prepare() {
  cd "$srcdir"
  for PATCH in $(ls *.patch); do
    patch -d $pkgname-$pkgver -p1 < "$PATCH"
  done
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
  mkdir -p "$pkgdir/usr/lib/systemd/user/dev-cec0.device.wants"
  ln -s ../plasma-remotecontrollers.service "$pkgdir/usr/lib/systemd/user/dev-cec0.device.wants/"
  mkdir -p "$pkgdir/usr/lib/systemd/user/gamescope-session.service.wants"
  ln -s ../plasma-remotecontrollers.service "$pkgdir/usr/lib/systemd/user/gamescope-session.service.wants/"
}
