# Maintainer: Felix Yan <felixonmars@archlinux.org>
# Maintainer: Antonio Rojas <arojas@archlinux.org>
# Contributor: Andrea Scarpino <andrea@archlinux.org>
# Contributor: David Edmundson <kde@davidedmundson.co.uk>

pkgname=kscreen
pkgver=5.23.5
pkgrel=3
# backport unplug/replug fixes from 5.26.0
pkgdesc='KDE screen management software'
arch=(x86_64)
url='https://kde.org/plasma-desktop/'
license=(LGPL)
depends=(libkscreen plasma-framework qt5-sensors)
makedepends=(extra-cmake-modules kcmutils)
groups=(plasma)
source=(https://download.kde.org/stable/plasma/$pkgver/$pkgname-$pkgver.tar.xz{,.sig}
        0001-X11-align-touchscreen-to-internal-display.patch
        0002-when-loading-defaults-don-t-forget-to-set-enablement.patch
        0003-loosen-the-duplication-check-a-tad.patch
        0004-fix-refresh-rate-list-not-being-updated.patch)
sha256sums=('d1032cfd442ee872db714522d8874a48050723ac22c47783c7478a11e47fb948'
            'SKIP'
            'SKIP'
            'SKIP'
            'SKIP'
            'SKIP')
validpgpkeys=('E0A3EB202F8E57528E13E72FD7574483BB57B18D'  # Jonathan Esk-Riddell <jr@jriddell.org>
              '0AAC775BB6437A8D9AF7A3ACFE0784117FBCE11D'  # Bhushan Shah <bshah@kde.org>
              'D07BD8662C56CB291B316EB2F5675605C74E02CF'  # David Edmundson <davidedmundson@kde.org>
              '1FA881591C26B276D7A5518EEAAF29B42A678C20') # Marco Martin <notmart@gmail.com>
options=(debug)

prepare() {
    patch -d $pkgbase-$pkgver -p1 < "${srcdir}/0001-X11-align-touchscreen-to-internal-display.patch"
    patch -d $pkgbase-$pkgver -p1 < "${srcdir}/0002-when-loading-defaults-don-t-forget-to-set-enablement.patch"
    patch -d $pkgbase-$pkgver -p1 < "${srcdir}/0003-loosen-the-duplication-check-a-tad.patch"
    patch -d $pkgbase-$pkgver -p1 < "${srcdir}/0004-fix-refresh-rate-list-not-being-updated.patch"
}

build() {
  cmake -B build -S $pkgname-$pkgver \
    -DBUILD_TESTING=OFF
  cmake --build build
}

package() {
  DESTDIR="$pkgdir" cmake --install build
}
