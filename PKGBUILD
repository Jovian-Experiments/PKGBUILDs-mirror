# Maintainer: Holo Team
# Contributor: Felix Yan <felixonmars@archlinux.org>
# Contributor: Antonio Rojas <arojas@archlinux.org>
# Contributor: Andrea Scarpino <andrea@archlinux.org>

pkgname=powerdevil
pkgver=6.8.2
_dirver=$(echo $pkgver | cut -d. -f1-3)
pkgrel=1.1 # Holo: Hide unactionable message to install power-profiles-daemon
pkgdesc='Manages the power consumption settings of a Plasma Shell'
arch=(x86_64)
url='https://kde.org/plasma-desktop/'
license=(LGPL-2.0-or-later)
depends=(ddcutil
         glibc
         plasma-activities
         kauth
         kcmutils
         kconfig
         kcoreaddons
         kcrash
         kdbusaddons
         kglobalaccel
         ki18n
         kidletime
         kirigami
         kitemmodels
         knotifications
         kpackage
         kservice
         kxmlgui
         libkscreen
         libplasma
         libstdc++
         plasma-workspace
         qcoro
         qt6-base
         qt6-declarative
         solid
         systemd-libs
         wayland)
makedepends=(extra-cmake-modules
             kdoctools
             plasma-wayland-protocols)
optdepends=('kinfocenter: for the Energy Information KCM'
            'power-profiles-daemon: power profiles support'
            'tlp: alternative power profiles support')
groups=(plasma)
source=(https://download.kde.org/stable/plasma/$_dirver/$pkgname-$pkgver.tar.xz{,.sig}
        0001-Hide-power-profiles-daemon-when-not-supported.patch  # See https://gitlab.steamos.cloud/holo-team/tasks/-/issues/1674
       )
sha256sums=('c663355adcfdfafe9824f48aa15881679fd71b0b16863a603a62ec0bce628d4a'
            'SKIP'
            '6d7063672c3d1900f012bc9f732cb8975eb38e19ba615da58cdf6f57ef08b39d')
validpgpkeys=('E0A3EB202F8E57528E13E72FD7574483BB57B18D'  # Jonathan Esk-Riddell <jr@jriddell.org>
              '0AAC775BB6437A8D9AF7A3ACFE0784117FBCE11D'  # Bhushan Shah <bshah@kde.org>
              'D07BD8662C56CB291B316EB2F5675605C74E02CF'  # David Edmundson <davidedmundson@kde.org>
              '1FA881591C26B276D7A5518EEAAF29B42A678C20') # Marco Martin <notmart@gmail.com>

prepare() {
  patch -p1 -d "$srcdir/$pkgname-$pkgver" -i "$srcdir/0001-Hide-power-profiles-daemon-when-not-supported.patch"
}

build() {
  cmake -B build  -S $pkgname-$pkgver \
    -DKDE_INSTALL_LIBEXECDIR=lib \
    -DBUILD_TESTING=OFF
  cmake --build build
}

package() {
  DESTDIR="$pkgdir" cmake --install build
}
