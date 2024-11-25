# Maintainer: Felix Yan <felixonmars@archlinux.org>
# Maintainer: Antonio Rojas <arojas@archlinux.org>
# Contributor: Andrea Scarpino <andrea@archlinux.org>

pkgname=kwin
pkgver=6.2.2
_dirver=$(echo $pkgver | cut -d. -f1-3)
pkgrel=1.1 # Holo: Allow xwayland to use libei without portal
pkgdesc='An easy to use, but flexible, composited Window Manager'
arch=(x86_64)
url='https://kde.org/plasma-desktop/'
license=(LGPL-2.0-or-later)
depends=(breeze
         gcc-libs
         glibc
         plasma-activities
         kauth
         kcmutils
         kcolorscheme
         kconfig
         kconfigwidgets
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
         libx11
         libxcb
         libxcvt
         libxi
         libxkbcommon
         libxkbcommon-x11
         mesa
         pipewire-session-manager
         libplasma
         qt6-5compat
         qt6-base
         qt6-declarative
         qt6-multimedia
         qt6-sensors
         qt6-svg
         qt6-tools
         qt6-wayland
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
optdepends=('maliit-keyboard: virtual keyboard for kwin-wayland')
groups=(plasma)
source=(https://download.kde.org/stable/plasma/$_dirver/$pkgname-$pkgver.tar.xz{,.sig}
        0001-Allow-passing-extra-environment-variables-to-Xwaylan.patch # Deck specific for X input
        0002-Allow-specifying-file-descriptors-that-are-passed-to.patch # Deck specific for X input
        0003-Enable-Xwayland-xtest-input-emulation-without-going-.patch # Deck specific for X input
        0004-Outputconfigurationstore-default-to-internal-display.patch # Deck specific for default scale
        0005-Fix-DPMS-Filter.patch # This can be dropped in 6.2.3 onwards
        )
install=$pkgname.install
sha256sums=('fb5c2ff3e8007722f3fa528872e6494dc21d48c8a6b632b748486389486bc061'
            'SKIP'
            '4c0f6dc62851371f63af725d09f2eeaf1a56f08ef6e8c16650d40212e84a8534'
            '5e5040d57cc6ec317ad7b2d4f4bcafb3b9632622f5ac6d0726699f55898ed788'
            'f7d91c5d14ef53585230db4621691b001a5a16be3a90f8ecd0f39db7dc403b9b'
            'SKIP'
            'SKIP')
validpgpkeys=('E0A3EB202F8E57528E13E72FD7574483BB57B18D'  # Jonathan Esk-Riddell <jr@jriddell.org>
              '0AAC775BB6437A8D9AF7A3ACFE0784117FBCE11D'  # Bhushan Shah <bshah@kde.org>
              'D07BD8662C56CB291B316EB2F5675605C74E02CF'  # David Edmundson <davidedmundson@kde.org>
              '1FA881591C26B276D7A5518EEAAF29B42A678C20') # Marco Martin <notmart@gmail.com>

prepare() {
  patch -p1 -d "$srcdir/$pkgname-$pkgver" -i "$srcdir/0001-Allow-passing-extra-environment-variables-to-Xwaylan.patch"
  patch -p1 -d "$srcdir/$pkgname-$pkgver" -i "$srcdir/0002-Allow-specifying-file-descriptors-that-are-passed-to.patch"
  patch -p1 -d "$srcdir/$pkgname-$pkgver" -i "$srcdir/0003-Enable-Xwayland-xtest-input-emulation-without-going-.patch"
  patch -p1 -d "$srcdir/$pkgname-$pkgver" -i "$srcdir/0004-Outputconfigurationstore-default-to-internal-display.patch"
  patch -p1 -d "$srcdir/$pkgname-$pkgver" -i "$srcdir/0005-Fix-DPMS-Filter.patch"
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
