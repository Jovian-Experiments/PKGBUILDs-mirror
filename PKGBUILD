# Maintainer: Felix Yan <felixonmars@archlinux.org>
# Maintainer: Antonio Rojas <arojas@archlinux.org>
# Contributor: Andrea Scarpino <andrea@archlinux.org>

pkgname=plasma-nm
pkgver=5.23.5
pkgrel=1.1
# Jupiter: Backport patches for https://gitlab.steamos.cloud/jupiter/tasks/-/issues/586
pkgdesc='Plasma applet written in QML for managing network connections'
arch=(x86_64)
url='https://kde.org/plasma-desktop/'
license=(GPL2)
depends=(plasma-workspace modemmanager-qt networkmanager-qt qca-qt5)
makedepends=(extra-cmake-modules openconnect)
optdepends=('openconnect: Cisco AnyConnect VPN plugin')
groups=(plasma)
source=(https://download.kde.org/stable/plasma/$pkgver/$pkgname-$pkgver.tar.xz{,.sig}
        0001-Add-Default-Connection-Type-Configuration.patch
        0002-Add-and-Activate.patch
       )
sha256sums=('4346067fafb34fbb71d39f88f8c8b52eb6b229e846072b610cbd934dfcb75393'
            'SKIP'
            '7b56e215abbd0ccec005aade57193f9b066d2f5a0bc24ee8950d5253c0749f46'
            '1d96bb525d76acba5acbf3e97aee28d63af5e448955712696c93f804f803f963'
           )
validpgpkeys=('E0A3EB202F8E57528E13E72FD7574483BB57B18D'  # Jonathan Esk-Riddell <jr@jriddell.org>
              '0AAC775BB6437A8D9AF7A3ACFE0784117FBCE11D'  # Bhushan Shah <bshah@kde.org>
              'D07BD8662C56CB291B316EB2F5675605C74E02CF'  # David Edmundson <davidedmundson@kde.org>
              '1FA881591C26B276D7A5518EEAAF29B42A678C20') # Marco Martin <notmart@gmail.com>

prepare() {
  patch -d $pkgbase-$pkgver -p1 --input="${srcdir}/0001-Add-Default-Connection-Type-Configuration.patch"
  patch -d $pkgbase-$pkgver -p1 --input="${srcdir}/0002-Add-and-Activate.patch"
}

build() {
  cmake -B build -S $pkgname-$pkgver \
    -DBUILD_TESTING=OFF
  cmake --build build
}

package() {
  DESTDIR="$pkgdir" cmake --install build
}

