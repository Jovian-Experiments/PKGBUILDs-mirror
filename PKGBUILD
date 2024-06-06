# Maintainer: Felix Yan <felixonmars@archlinux.org>
# Maintainer: Antonio Rojas <arojas@archlinux.org>
# Contributor: Andrea Scarpino <andrea@archlinux.org>
# Contributor: Alexey D. <lq07829icatm at rambler.ru>

pkgbase=plasma-workspace
pkgname=(plasma-workspace plasma-wayland-session)
pkgver=5.27.10
_dirver=$(echo $pkgver | cut -d. -f1-3)
pkgrel=2.2
pkgdesc='KDE Plasma Workspace'
arch=(x86_64)
url='https://kde.org/plasma-desktop/'
license=(LGPL)
depends=(knotifyconfig5 ksystemstats ktexteditor5 libqalculate kde-cli-tools appstream-qt5
         xorg-xrdb xorg-xsetroot kactivitymanagerd kholidays5 xorg-xmessage milou prison5 kwin
         plasma-integration kpeople5 kactivities-stats5 kquickcharts5 kuserfeedback5 kpipewire
         accountsservice kio-extras kio-fuse qt5-tools oxygen-sounds)
makedepends=(extra-cmake-modules kdoctools5 gpsd baloo5 networkmanager-qt5 plasma-wayland-protocols wayland-protocols kunitconversion5)
groups=(plasma)
source=(https://download.kde.org/stable/plasma/$_dirver/$pkgbase-$pkgver.tar.xz{,.sig} kde.pam
        appstream-1.0.patch
        0001-Authenticate-local-clients.patch
        0002-Remove-iceauth-dependency.patch
        )
sha256sums=('525dc164c61a6730f33d54ff5013d57184b9d671786fe898ca7e054426359778'
            'SKIP'
            '00090291204baabe9d6857d3b1419832376dd2e279087d718b64792691e86739'
            'e3068a5709711dc54809b0280a59ec3ab6bc3b7ad0f0d93246e40d1daa1dc45e'
            '88a47f8c88535241b437e876a35234f6e6f5ab5f0e424df601ece051c772ac3d'
            '88d2f254c94f8aca78cc1886918125afff55679ae253bb271c6b8e903577f620'
            )
validpgpkeys=('E0A3EB202F8E57528E13E72FD7574483BB57B18D'  # Jonathan Esk-Riddell <jr@jriddell.org>
              '0AAC775BB6437A8D9AF7A3ACFE0784117FBCE11D'  # Bhushan Shah <bshah@kde.org>
              'D07BD8662C56CB291B316EB2F5675605C74E02CF'  # David Edmundson <davidedmundson@kde.org>
              '1FA881591C26B276D7A5518EEAAF29B42A678C20') # Marco Martin <notmart@gmail.com>

prepare() {
  patch -d $pkgbase-$pkgver -p1 < appstream-1.0.patch # Support appstream 1.0
  patch -d $pkgbase-$pkgver -p1 < 0001-Authenticate-local-clients.patch # Security fix, drop in 5.27.11
  patch -d $pkgbase-$pkgver -p1 < 0002-Remove-iceauth-dependency.patch # Security fix, drop in 5.27.11
}

build() {

  # GLIBC_LOCALE_* settings are overriden due to Steam differences
  # with the read only disk.
  # See documentation with CMakeLists.txt of plasma-workspace for details

  cmake -B build -S $pkgbase-$pkgver \
    -DCMAKE_INSTALL_LIBEXECDIR=lib \
    -DGLIBC_LOCALE_PREGENERATED=ON \
    -DGLIBC_LOCALE_GEN=OFF \
    -DBUILD_TESTING=OFF
  cmake --build build
}

package_plasma-workspace() {
  optdepends=('plasma-workspace-wallpapers: additional wallpapers'
              'gpsd: GPS based geolocation' 'networkmanager-qt5: IP based geolocation'
              'kdepim-addons: displaying PIM events in the calendar'
              'appmenu-gtk-module: global menu support for GTK2 and some GTK3 applications'
              'baloo5: Baloo search runner' 'discover: manage applications installation from the launcher')
  backup=('etc/pam.d/kde')

  DESTDIR="$pkgdir" cmake --install build

  install -Dm644 "$srcdir"/kde.pam "$pkgdir"/etc/pam.d/kde

  # Split plasma-wayland scripts
  rm -r "$pkgdir"/usr/share/wayland-sessions
}

package_plasma-wayland-session() {
  pkgdesc='Plasma Wayland session'
  depends=(plasma-workspace qt5-wayland kwayland-integration xorg-xwayland)
  groups=()

  install -Dm644 build/login-sessions/plasmawayland.desktop "$pkgdir"/usr/share/wayland-sessions/plasmawayland.desktop
}
