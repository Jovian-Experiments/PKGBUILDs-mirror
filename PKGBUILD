# Maintainer: Felix Yan <felixonmars@archlinux.org>
# Maintainer: Antonio Rojas <arojas@archlinux.org>
# Contributor: Andrea Scarpino <andrea@archlinux.org>

pkgname=bluedevil # Removed outdated workaround that broke newer Bluetooth device pairings
pkgver=6.4.3
_dirver=$(echo $pkgver | cut -d. -f1-3)
pkgrel=2
epoch=1
pkgdesc='Integrate the Bluetooth technology within KDE workspace and applications'
arch=(x86_64)
url='https://kde.org/plasma-desktop/'
license=(GPL-2.0-or-later)
depends=(bluez-qt
         gcc-libs
         glibc
         kcmutils
         kconfig
         kcoreaddons
         kdbusaddons
         kdeclarative
         ki18n
         kio
         kirigami
         kjobwidgets
         knotifications
         kservice
         ksvg
         kwidgetsaddons
         kwindowsystem
         libplasma
         qt6-base
         qt6-declarative)
makedepends=(extra-cmake-modules
             kdoctools)
optdepends=('bluez-obex: file transfer'
            'pulseaudio-bluetooth: to connect to A2DP profile')
groups=(plasma)
source=(https://download.kde.org/stable/plasma/$_dirver/$pkgname-$pkgver.tar.xz{,.sig}
        0001-Revert-fix-pairing-bug.patch # Potentially drop in Plasma 6.6. Track at https://invent.kde.org/plasma/bluedevil/-/merge_requests/227
       )
sha256sums=('2760dbbd3ee785ce493d39f8f6272f479db184076a6e30f1f4646afbd8ca331d'
            'SKIP'
            '5a055b2e7110d648f454b50e6cee7df872a7ff7c16af94fe1007311d4e83aef6')
validpgpkeys=('E0A3EB202F8E57528E13E72FD7574483BB57B18D'  # Jonathan Esk-Riddell <jr@jriddell.org>
              '0AAC775BB6437A8D9AF7A3ACFE0784117FBCE11D'  # Bhushan Shah <bshah@kde.org>
              'D07BD8662C56CB291B316EB2F5675605C74E02CF'  # David Edmundson <davidedmundson@kde.org>
              '1FA881591C26B276D7A5518EEAAF29B42A678C20') # Marco Martin <notmart@gmail.com>

build() {
  cmake -B build  -S $pkgname-$pkgver \
    -DCMAKE_INSTALL_LIBEXECDIR=lib \
    -DBUILD_TESTING=OFF
  cmake --build build
}

prepare() {
  patch -p1 -d "$srcdir/$pkgname-$pkgver" -i "$srcdir/0001-Revert-fix-pairing-bug.patch"
}

package() {
  DESTDIR="$pkgdir" cmake --install build
}
