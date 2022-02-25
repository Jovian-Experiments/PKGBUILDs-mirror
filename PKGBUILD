# Maintainer: Felix Yan <felixonmars@archlinux.org>
# Maintainer: Antonio Rojas <arojas@archlinux.org>
# Contributor: Andrea Scarpino <andrea@archlinux.org>
# Contributor: Alexey D. <lq07829icatm at rambler.ru>

pkgbase=plasma-workspace
pkgname=(plasma-workspace plasma-wayland-session)
pkgver=5.23.5
pkgrel=3
pkgdesc='KDE Plasma Workspace'
arch=(x86_64)
url='https://kde.org/plasma-desktop/'
license=(LGPL)
depends=(knotifyconfig ksystemstats ktexteditor libqalculate kde-cli-tools appstream-qt
         xorg-xrdb xorg-xsetroot kactivitymanagerd kholidays xorg-xmessage milou prison kwin
         plasma-integration kpeople kactivities-stats libkscreen kquickcharts kuserfeedback kio-extras kio-fuse)
makedepends=(extra-cmake-modules kdoctools gpsd baloo networkmanager-qt plasma-wayland-protocols kunitconversion kinit)
groups=(plasma)
source=(https://download.kde.org/stable/plasma/$pkgver/$pkgbase-$pkgver.tar.xz{,.sig} kde.pam
        https://invent.kde.org/plasma/plasma-workspace/-/commit/70d23b89.patch
        https://invent.kde.org/plasma/plasma-workspace/-/commit/926f8647.patch
        0001-Load-additional-actions-for-app-entries-in-applicati.patch
        steam.desktop)
sha256sums=('2ebee6ab2f10cabc350e0f75a0d8462ae0b7616a795d078f6bb5765396052575'
            'SKIP'
            '00090291204baabe9d6857d3b1419832376dd2e279087d718b64792691e86739'
            '810660c3d7948c21c61f8d4c7d604ca7cb51c85e1a41c6225d1f39c72feae808'
            'fe5ae91bc2c5e1b9021523efec60dc7740285e2c74684639e8238e9df9f58572'
            '20617818d22a655236a30b7ec75ddf3c9917e2efa696884b84d9a27fa3159dab'
            'e7a1cf78b2a2bc4217aec19fed65d88ecf26b4150ef7b8cc508a63c1a43b5804')
validpgpkeys=('E0A3EB202F8E57528E13E72FD7574483BB57B18D'  # Jonathan Esk-Riddell <jr@jriddell.org>
              '0AAC775BB6437A8D9AF7A3ACFE0784117FBCE11D'  # Bhushan Shah <bshah@kde.org>
              'D07BD8662C56CB291B316EB2F5675605C74E02CF'  # David Edmundson <davidedmundson@kde.org>
              '1FA881591C26B276D7A5518EEAAF29B42A678C20') # Marco Martin <notmart@gmail.com>

prepare() {
  patch -d $pkgbase-$pkgver -p1 < 70d23b89.patch # Remove implicit kinit dependency on shell runner
  patch -d $pkgbase-$pkgver -p1 < 926f8647.patch # Fix missing taskbar thumbnails on Wayland
  patch -d $pkgbase-$pkgver -p1 --input="${srcdir}/0001-Load-additional-actions-for-app-entries-in-applicati.patch"
}

build() {
  cmake -B build -S $pkgbase-$pkgver \
    -DCMAKE_INSTALL_LIBEXECDIR=lib \
    -DBUILD_TESTING=OFF \
    -DCMAKE_INSTALL_PREFIX=/usr
  cmake --build build
}

package_plasma-workspace() {
  optdepends=('plasma-workspace-wallpapers: additional wallpapers'
              'gpsd: GPS based geolocation' 'networkmanager-qt: IP based geolocation'
              'kdepim-addons: displaying PIM events in the calendar'
              'appmenu-gtk-module: global menu support for GTK2 and some GTK3 applications'
              'baloo: Baloo search runner' 'discover: manage applications installation from the launcher')
  backup=('etc/pam.d/kde')

  DESTDIR="$pkgdir" cmake --install build

  install -Dm644 "$srcdir"/kde.pam "$pkgdir"/etc/pam.d/kde
  install -D -m644 "$srcdir"/steam.desktop "$pkgdir"/usr/share/plasma/kickeractions/steam.desktop

  # Split plasma-wayland scripts
  rm -r "$pkgdir"/usr/share/wayland-sessions
}

package_plasma-wayland-session() {
  pkgdesc='Plasma Wayland session'
  depends=(plasma-workspace qt5-wayland kwayland-integration xorg-xwayland)
  groups=()

  install -Dm644 build/login-sessions/plasmawayland.desktop "$pkgdir"/usr/share/wayland-sessions/plasmawayland.desktop
}
