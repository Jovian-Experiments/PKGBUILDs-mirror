# Maintainer: Felix Yan <felixonmars@archlinux.org>
# Maintainer: Antonio Rojas <arojas@archlinux.org>
# Contributor: Andrea Scarpino <andrea@archlinux.org>

pkgname=plasma-desktop
pkgver=5.27.5
_dirver=$(echo $pkgver | cut -d. -f1-3)
pkgrel=1.1
pkgdesc='KDE Plasma Desktop'
arch=(x86_64)
url='https://kde.org/plasma-desktop/'
license=(LGPL)
source=(https://download.kde.org/stable/plasma/$_dirver/$pkgname-$pkgver.tar.xz{,.sig}
        dont-track-drops-recursively.patch # Holo: Avoid recursive tracking when dragging folders onto desktop (Fixed in 5.27.9) 
        )
depends=(gawk kdelibs4support polkit-kde-agent kmenuedit systemsettings powerdevil baloo xdg-user-dirs)
optdepends=('plasma-nm: Network manager applet'
            'kscreen: screen management'
            'ibus: kimpanel IBUS support'
            'scim: kimpanel SCIM support'
            'kaccounts-integration: OpenDesktop integration plugin'
            'packagekit-qt5: to install new krunner plugins')
makedepends=(extra-cmake-modules kdoctools xf86-input-evdev xf86-input-synaptics xf86-input-libinput xorg-server-devel
             scim kdesignerplugin kaccounts-integration intltool packagekit-qt5 kinit wayland-protocols libibus)
groups=(plasma)
sha256sums=('4f2b573134658f640717d6ee67eaee41d9df4c578856016efa769b4415e91cb1'
            'SKIP'
            '375466b965c9206682aa2e43ec7848bfce0d510bf6477a8c03e9d30a96f6db31')
validpgpkeys=('E0A3EB202F8E57528E13E72FD7574483BB57B18D'  # Jonathan Esk-Riddell <jr@jriddell.org>
              '0AAC775BB6437A8D9AF7A3ACFE0784117FBCE11D'  # Bhushan Shah <bshah@kde.org>
              'D07BD8662C56CB291B316EB2F5675605C74E02CF'  # David Edmundson <davidedmundson@kde.org>
              '1FA881591C26B276D7A5518EEAAF29B42A678C20') # Marco Martin <notmart@gmail.com>

prepare() {
  patch -d $pkgbase-$pkgver -p1 --input="${srcdir}/dont-track-drops-recursively.patch"
}

build() {
  cmake -B build -S $pkgname-$pkgver \
    -DCMAKE_INSTALL_LIBEXECDIR=lib \
    -DBUILD_TESTING=OFF
  cmake --build build
}

package() {
  DESTDIR="$pkgdir" cmake --install build
}
