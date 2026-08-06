# Maintainer: Holo Team
# Contributor: Felix Yan <felixonmars@archlinux.org>
# Contributor: Antonio Rojas <arojas@archlinux.org>
# Contributor: Andrea Scarpino <andrea@archlinux.org>

pkgname=kwin
pkgver=6.7.3
_dirver=$(echo $pkgver | cut -d. -f1-3)
pkgrel=1.2 # support libei 1.6 features
pkgdesc='An easy to use, but flexible, Wayland compositor'
arch=(x86_64)
url='https://kde.org/plasma-desktop/'
license=(LGPL-2.0-or-later)
depends=(aurorae
         breeze
         glibc
         iio-sensor-proxy
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
         knighttime
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
         libevdev
         libgcc
         libinput
         libpipewire
         libqaccessibilityclient-qt6
         libstdc++
         libxcb
         libxcvt
         libxkbcommon
         mesa
         milou
         pipewire-session-manager
         libplasma
         qt6-5compat
         qt6-base
         qt6-declarative
         qt6-svg
         qt6-tools
         systemd-libs
         vulkan-icd-loader
         wayland
         xcb-util-keysyms
         xcb-util-wm)
makedepends=(extra-cmake-modules
             kdoctools
             krunner
             plasma-wayland-protocols
             python
             vulkan-headers
             wayland-protocols
             xorg-xwayland)
optdepends=('plasma-keyboard: virtual keyboard')
groups=(plasma)
source=(https://download.kde.org/stable/plasma/$_dirver/$pkgname-$pkgver.tar.xz{,.sig}
        0002-Load-current-brightness-from-device.patch # Keep screen brightness from gamescope, track at https://bugs.kde.org/show_bug.cgi?id=508163
        0003-Outputconfigurationstore-default-to-internal-display.patch # Deck specific for default scale
        0006-inputmethod-Skip-input-events-from-fake-input.patch #Currently deck specific, a workaround for the Steam OSK. Test CJK input with both SteamOSK and a physical keyboard both work before dropping
        0011-Eis-Support-1.6-additions.patch # relies on a libei 1.6 feature that we patch in on deck; Drop in 6.8
        )
sha256sums=('345b45d400884cc6b00f4b3585cc056aa2780f32afe2df394d20c5a98273c559'
            'SKIP'
            '81aabc16f054ba3cd47d0fe5d9169df17cd1f14d7dfc324786e86cbe08c84b48'
            '9417723b2a2c2ff81b914707edf6dd759ec1fa729eb80fea0719e1722b004a55'
            'bf08aae2967d3cd4202ee27004eff2feedc98163626fd98f96b7d2acae40dc38'
            '36ba3e57ac5ef8d3e5b4f17ad3623231d60267077bdcfb5566deb07fd103d11d')

validpgpkeys=('E0A3EB202F8E57528E13E72FD7574483BB57B18D'  # Jonathan Esk-Riddell <jr@jriddell.org>
              '0AAC775BB6437A8D9AF7A3ACFE0784117FBCE11D'  # Bhushan Shah <bshah@kde.org>
              'D07BD8662C56CB291B316EB2F5675605C74E02CF'  # David Edmundson <davidedmundson@kde.org>
              '90A968ACA84537CC27B99EAF2C8DF587A6D4AAC1'  # Nicolas Fella <nicolas.fella@kde.org>
              '1FA881591C26B276D7A5518EEAAF29B42A678C20') # Marco Martin <notmart@gmail.com>

prepare() {
  patch -p1 -d "$srcdir/$pkgname-$pkgver" -i "$srcdir/0002-Load-current-brightness-from-device.patch"
  patch -p1 -d "$srcdir/$pkgname-$pkgver" -i "$srcdir/0003-Outputconfigurationstore-default-to-internal-display.patch"
  patch -p1 -d "$srcdir/$pkgname-$pkgver" -i "$srcdir/0006-inputmethod-Skip-input-events-from-fake-input.patch"
  patch -p1 -d "$srcdir/$pkgname-$pkgver" -i "$srcdir/0011-Eis-Support-1.6-additions.patch"
}

build() {
  cmake -B build  -S $pkgname-$pkgver \
    -DCMAKE_INSTALL_LIBEXECDIR=lib \
    -DBUILD_TESTING=OFF
  cmake --build build
}

package() {
  DESTDIR="$pkgdir" cmake --install build
  setcap CAP_SYS_NICE=+ep "$pkgdir"/usr/bin/kwin_wayland
}
