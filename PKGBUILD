# Maintainer: Felix Yan <felixonmars@archlinux.org>
# Maintainer: Antonio Rojas <arojas@archlinux.org>
# Contributor: Andrea Scarpino <andrea@archlinux.org>

pkgname=kscreen
pkgver=6.2.5
_dirver=$(echo $pkgver | cut -d. -f1-3)
pkgrel=2 #Holo backport osd/plasmoid action fixes
pkgdesc='KDE screen management software'
arch=(x86_64)
url='https://kde.org/plasma-desktop/'
license=(LGPL-2.0-or-later)
depends=(gcc-libs
         glibc
         kcmutils
         kconfig
         kcoreaddons
         kdbusaddons
         ki18n
         kirigami
         ksvg
         kwindowsystem
         layer-shell-qt
         libkscreen
         libx11
         libxcb
         libxi
         libplasma
         plasma5support
         qt6-base
         qt6-declarative
         qt6-sensors)
makedepends=(extra-cmake-modules)
groups=(plasma)
source=(https://download.kde.org/stable/plasma/$_dirver/$pkgname-$pkgver.tar.xz{,.sig}
        0001-Take-rotation-into-account-when-applying-osd-actions.patch # Drop when updating to Plasma 6.4
        0002-Make-common-a-library.patch # Drop when updating to Plasma 6.4
        0003-Move-output-to-common.patch # Drop when updating to Plasma 6.4
        0004-Reapply-rotation-on-X11-when-applying-osd-action.patch # Drop when updating to Plasma 6.4
        0005-Disable-clone-action.patch # Revisit when updating to Plasma 6.4
)
sha256sums=('6237c47fe70384d10e6f20d7f058c6aacca51a493da928077fcec91b0ef69642'
            'SKIP'
            'f35477ff434418d9feb58422a268cd92f60abcd3ea77315f4f7308f335b860d9'
            '8256cc6fc1d972c5c9088fbb7c65765fe2a893364a6b7c24513f8711a6897ba2'
            '0577cd03f3f2a86af4ad1c51ca39281c4071bbf4f3131fc57152a331ad655ee9'
            '0e24c656e366924db95ef6ddb8dc540de63b10d92596752f4e3d95f9eaa96aaf'
            '2c93084d12a51a7f82991f70b036bddad5988feba1e02b98051a6418eb5d2ad5')
validpgpkeys=('E0A3EB202F8E57528E13E72FD7574483BB57B18D'  # Jonathan Esk-Riddell <jr@jriddell.org>
              '0AAC775BB6437A8D9AF7A3ACFE0784117FBCE11D'  # Bhushan Shah <bshah@kde.org>
              'D07BD8662C56CB291B316EB2F5675605C74E02CF'  # David Edmundson <davidedmundson@kde.org>
              '1FA881591C26B276D7A5518EEAAF29B42A678C20') # Marco Martin <notmart@gmail.com>

prepare() {
 patch -p1 -d "$srcdir/$pkgname-$pkgver" -i "$srcdir/0001-Take-rotation-into-account-when-applying-osd-actions.patch"
 patch -p1 -d "$srcdir/$pkgname-$pkgver" -i "$srcdir/0002-Make-common-a-library.patch"
 patch -p1 -d "$srcdir/$pkgname-$pkgver" -i "$srcdir/0003-Move-output-to-common.patch"
 patch -p1 -d "$srcdir/$pkgname-$pkgver" -i "$srcdir/0004-Reapply-rotation-on-X11-when-applying-osd-action.patch"
 patch -p1 -d "$srcdir/$pkgname-$pkgver" -i "$srcdir/0005-Disable-clone-action.patch"
}

build() {
  cmake -B build  -S $pkgname-$pkgver \
    -DBUILD_TESTING=OFF \
    -DCMAKE_INSTALL_LIBEXECDIR=lib
  cmake --build build
}

package() {
  DESTDIR="$pkgdir" cmake --install build
}
