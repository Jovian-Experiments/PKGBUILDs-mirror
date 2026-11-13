# Maintainer: Holo Team
# Contributor: Felix Yan <felixonmars@archlinux.org>
# Contributor: Antonio Rojas <arojas@archlinux.org>
# Contributor: Andrea Scarpino <andrea@archlinux.org>

pkgname=kwin
pkgver=6.8.2
_dirver=$(echo $pkgver | cut -d. -f1-3)
pkgrel=1.3
pkgdesc='An easy to use, but flexible, Wayland compositor'
arch=(x86_64)
url='https://kde.org/plasma-desktop/'
license=(LGPL-2.0-or-later)
depends=(
  aurorae
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
  krunner
  'kscreenlocker>=6.8.2'  # Holo: Enforce the correct rebuild order
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
  xcb-util-wm
)
makedepends=(
  extra-cmake-modules
  kdoctools
  krunner
  plasma-wayland-protocols
  python
  vulkan-headers
  wayland-protocols
  xorg-xwayland
)
optdepends=(
  'plasma-keyboard: virtual keyboard'
)
groups=(
  plasma
)
source=(
  https://download.kde.org/stable/plasma/$_dirver/$pkgname-$pkgver.tar.xz{,.sig}

        0002-Load-current-brightness-from-device.patch # Keep screen brightness from gamescope, track at https://bugs.kde.org/show_bug.cgi?id=508163
        0006-inputmethod-Skip-input-events-from-fake-input.patch #Currently deck specific, a workaround for the Steam OSK. Test CJK input with both SteamOSK and a physical keyboard both work before dropping
        0007-backends-libinput-list-devices-during-setup.patch
        0008-outputconfigurationstore-improve-the-default-scale-f.patch
        )
sha256sums=('ea5e68d957c7d70abed97222a592d4445fda29129e20942658badd224ee138b4'
            'SKIP'
            '81aabc16f054ba3cd47d0fe5d9169df17cd1f14d7dfc324786e86cbe08c84b48'
            'bf08aae2967d3cd4202ee27004eff2feedc98163626fd98f96b7d2acae40dc38'
            '91289ca857da621c4ece6fd24b51f0c43e8bf31dd567da261af0c7e71a4093a9'
            'c2d164309123c2a743c2d2cd82031e031eb0a924df0eb06e9527c8e4911980e0')

validpgpkeys=('E0A3EB202F8E57528E13E72FD7574483BB57B18D'  # Jonathan Esk-Riddell <jr@jriddell.org>
              '0AAC775BB6437A8D9AF7A3ACFE0784117FBCE11D'  # Bhushan Shah <bshah@kde.org>
              'D07BD8662C56CB291B316EB2F5675605C74E02CF'  # David Edmundson <davidedmundson@kde.org>
              '90A968ACA84537CC27B99EAF2C8DF587A6D4AAC1'  # Nicolas Fella <nicolas.fella@kde.org>
              '1FA881591C26B276D7A5518EEAAF29B42A678C20') # Marco Martin <notmart@gmail.com>

prepare() {
  patch -p1 -d "$srcdir/$pkgname-$pkgver" -i "$srcdir/0002-Load-current-brightness-from-device.patch"
  patch -p1 -d "$srcdir/$pkgname-$pkgver" -i "$srcdir/0006-inputmethod-Skip-input-events-from-fake-input.patch"
  patch -p1 -d "$srcdir/$pkgname-$pkgver" -i "$srcdir/0007-backends-libinput-list-devices-during-setup.patch"
  patch -p1 -d "$srcdir/$pkgname-$pkgver" -i "$srcdir/0008-outputconfigurationstore-improve-the-default-scale-f.patch"
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
