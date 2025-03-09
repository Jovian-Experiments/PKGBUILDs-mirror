# Maintainer: Felix Yan <felixonmars@archlinux.org>
# Maintainer: Antonio Rojas <arojas@archlinux.org>
# Contributor: Andrea Scarpino <andrea@archlinux.org>

pkgname=kwin
pkgver=6.2.5
_dirver=$(echo $pkgver | cut -d. -f1-3)
pkgrel=1.2 # Holo: Allow xwayland to use libei without portal
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
        0005-x11-Update-XStacking-order-when-adding-override-redi.patch # Bugfix backport can be dropped after 6.3.3
        )
install=$pkgname.install
sha256sums=('5cc450a6e41105c8c49929b72550b331237f96aafb294690f4707bdc5f776848'
            'SKIP'
            'efe97260d2d157c867d26eb589faae6b47c41554e78ff83ff19b94d03d8e38ea'
            '4ebbde0ee2e1f013a2b64673d25faf44173b2c40799cbbdb5dfb90740b606006'
            'ba0ef9198be28a180804b905026419efd88ea9582c93c6f6c851732254ba2890'
            '9417723b2a2c2ff81b914707edf6dd759ec1fa729eb80fea0719e1722b004a55'
            '8b1f3908c8cc3e1de0c73c94f5947970962d23fef4fedf40421268eefb4f62e3')
validpgpkeys=('E0A3EB202F8E57528E13E72FD7574483BB57B18D'  # Jonathan Esk-Riddell <jr@jriddell.org>
              '0AAC775BB6437A8D9AF7A3ACFE0784117FBCE11D'  # Bhushan Shah <bshah@kde.org>
              'D07BD8662C56CB291B316EB2F5675605C74E02CF'  # David Edmundson <davidedmundson@kde.org>
              '1FA881591C26B276D7A5518EEAAF29B42A678C20') # Marco Martin <notmart@gmail.com>

prepare() {
  patch -p1 -d "$srcdir/$pkgname-$pkgver" -i "$srcdir/0001-Allow-passing-extra-environment-variables-to-Xwaylan.patch"
  patch -p1 -d "$srcdir/$pkgname-$pkgver" -i "$srcdir/0002-Allow-specifying-file-descriptors-that-are-passed-to.patch"
  patch -p1 -d "$srcdir/$pkgname-$pkgver" -i "$srcdir/0003-Enable-Xwayland-xtest-input-emulation-without-going-.patch"
  patch -p1 -d "$srcdir/$pkgname-$pkgver" -i "$srcdir/0004-Outputconfigurationstore-default-to-internal-display.patch"
  patch -p1 -d "$srcdir/$pkgname-$pkgver" -i "$srcdir/0005-x11-Update-XStacking-order-when-adding-override-redi.patch"
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
