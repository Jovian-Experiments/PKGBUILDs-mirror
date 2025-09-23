# Maintainer: Holo Team
# Contributor: Felix Yan <felixonmars@archlinux.org>
# Contributor: Antonio Rojas <arojas@archlinux.org>
# Contributor: Andrea Scarpino <andrea@archlinux.org>

pkgname=kwin
pkgver=6.4.3
_dirver=$(echo $pkgver | cut -d. -f1-3)
pkgrel=1.5 # Holo: Default scale fix
pkgdesc='An easy to use, but flexible, Wayland compositor'
arch=(x86_64)
url='https://kde.org/plasma-desktop/'
license=(LGPL-2.0-or-later)
depends=(aurorae
         breeze
         gcc-libs
         glibc
         plasma-activities
         kauth
         kcmutils
         kcolorscheme
         kconfig
         kcoreaddons
         kcrash
         kdbusaddons
         kdeclarative
         kdecoration
         kglobalaccel
         kglobalacceld
         kguiaddons
         ki18n
         kidletime
         kirigami
         kitemmodels
         knewstuff
         knotifications
         kpackage
         kquickcharts
         kscreenlocker
         kservice
         ksvg
         kwayland
         kwidgetsaddons
         kwindowsystem
         kxmlgui
         lcms2
         libcanberra
         libdisplay-info
         libdrm
         libei
         libepoxy
         libinput
         libpipewire
         libqaccessibilityclient-qt6
         libxcb
         libxcvt
         libxkbcommon
         mesa
         pipewire-session-manager
         libplasma
         qt6-5compat
         qt6-base
         qt6-declarative
         qt6-sensors
         qt6-svg
         qt6-tools
         systemd-libs
         wayland
         xcb-util-cursor
         xcb-util-keysyms
         xcb-util-wm)
makedepends=(extra-cmake-modules
             kdoctools
             krunner
             plasma-wayland-protocols
             python
             wayland-protocols
             xorg-xwayland)
optdepends=('maliit-keyboard: virtual keyboard')
groups=(plasma)
source=(https://download.kde.org/stable/plasma/$_dirver/$pkgname-$pkgver.tar.xz{,.sig}
        0001-backends-libinput-prefer-output-UUID-over-output-nam.patch # Drop in 6.5
        0002-Load-current-brightness-from-device.patch # Keep screen brightness from gamescope, track at https://bugs.kde.org/show_bug.cgi?id=508163
        0003-Outputconfigurationstore-default-to-internal-display.patch # Deck specific for default scale
        0004-simulate-full-keyboard-handling-in-testFakeEve.patch # Drop in 6.5
        0005-Support-arbitrary-keysyms-in-libei.patch # Currently deck specific, relies on unreleased libei feature that we also patch
        )
install=$pkgname.install
sha256sums=('a13568c918eca7803eb44a3a2778b860edc3f03b36797851c4f3aeeed4b502a8'
            'SKIP'
            '4c24a5b9d2b181f3c4d7f4927f760d2302702eeae67592112bcb35a6c1d3a0af'
            '887985706783d2658637548c8a63220397b9ebbd8fc425839d99c6138e8f19b8'
            '9417723b2a2c2ff81b914707edf6dd759ec1fa729eb80fea0719e1722b004a55'
            '31997f384c70c673624858bd0957a7a136afbc03cd95780e1e32cc7baf00d5e9'
            '5c9659a4228a39c8011491484ad31bcefb2a1fcffc75f2c18dbb4718212f49a5')
validpgpkeys=('E0A3EB202F8E57528E13E72FD7574483BB57B18D'  # Jonathan Esk-Riddell <jr@jriddell.org>
              '0AAC775BB6437A8D9AF7A3ACFE0784117FBCE11D'  # Bhushan Shah <bshah@kde.org>
              'D07BD8662C56CB291B316EB2F5675605C74E02CF'  # David Edmundson <davidedmundson@kde.org>
              '90A968ACA84537CC27B99EAF2C8DF587A6D4AAC1'  # Nicolas Fella <nicolas.fella@kde.org>
              '1FA881591C26B276D7A5518EEAAF29B42A678C20') # Marco Martin <notmart@gmail.com>

prepare() {
  patch -p1 -d "$srcdir/$pkgname-$pkgver" -i "$srcdir/0001-backends-libinput-prefer-output-UUID-over-output-nam.patch"
  patch -p1 -d "$srcdir/$pkgname-$pkgver" -i "$srcdir/0002-Load-current-brightness-from-device.patch"
  patch -p1 -d "$srcdir/$pkgname-$pkgver" -i "$srcdir/0003-Outputconfigurationstore-default-to-internal-display.patch"
  patch -p1 -d "$srcdir/$pkgname-$pkgver" -i "$srcdir/0004-simulate-full-keyboard-handling-in-testFakeEve.patch"
  patch -p1 -d "$srcdir/$pkgname-$pkgver" -i "$srcdir/0005-Support-arbitrary-keysyms-in-libei.patch"
}

build() {
  cmake -B build  -S $pkgname-$pkgver \
    -DCMAKE_INSTALL_LIBEXECDIR=lib \
    -DBUILD_TESTING=OFF
  cmake --build build
}

package() {
  DESTDIR="$pkgdir" cmake --install build
}
