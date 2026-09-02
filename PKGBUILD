# Maintainer: Holo Team
# Contributor: Antonio Rojas <arojas@archlinux.org>

pkgname=drkonqi
pkgver=6.7.3
_dirver=$(echo $pkgver | cut -d. -f1-3)
pkgrel=2
pkgdesc='The KDE crash handler'
arch=(x86_64)
url='https://kde.org/plasma-desktop/'
license=(GPL-2.0-or-later)
depends=(elfutils
         gdb
         glibc
         kcmutils
         kconfig
         kcoreaddons
         kcrash
         ki18n
         kidletime
         kio
         kirigami
         kitemmodels
         knotifications
         kservice
         kstatusnotifieritem
         kwallet
         kwidgetsaddons
         kwindowsystem
         libgcc
         libstdc++
         polkit-qt6
         python
         python-psutil
         python-pygdbmi
         python-sentry_sdk
         qt6-base
         qt6-declarative
         syntax-highlighting
         systemd-libs)
makedepends=(extra-cmake-modules)
groups=(plasma)
source=(https://download.kde.org/stable/plasma/$_dirver/$pkgname-$pkgver.tar.xz{,.sig}
        0001-launcher.socket-bump-feature-set-to-limit-activation.patch # Drop after 6.8
        0002-launcher.socket-attach-the-unit-to-plasma.patch # Drop after 6.8
        0003-launcher.service-ensure-it-doesn-t-participate-in-se.patch # Drop after 6.8
        0004-launcher.socket-correctly-change-wantedby.patch # Drop after 6.8
        0005-launcher.socket-loosen-grip-on-plasma-core.target.patch # Drop after 6.8
        0006-cleanup.timer-do-not-start-outside-plasma.patch # Drop after 6.8
        0007-postman.path-do-not-start-outside-plasma.patch # Drop after 6.8
        0008-coredump-don-t-process-crashes-of-our-own-binaries.patch # Drop after 6.7.5
        )
sha256sums=('d2e2c158c0e3f7e47f1a2529c30caffc3bff1aa8398dd6dff8c9645244f9ce26'
            'SKIP'
            'e5c60df24192bc46214e3cec23567bd436151d05344a910bf17cd2c5d2722d31'
            'f6a2368a4a6c744f5c09ad2cb0cfcef63e1472aa66e1ea1c397571f0926088ce'
            'f9e2c24ec6e39cba8fb03aba5ae3f9835c1d537675f17068962afeeec1d66e08'
            '6cf509781317511d98684cc88086ef7ff84252c68c87987597c85a3344a612e2'
            '0ae347615b4621ca101bc895696db5e4ec6c11f0eb989951b843f58dcac0c9d7'
            'c2831925110f51e3eb145550bb3d9fc53a133eb9a446b909d009fbcebda5bd06'
            '74bed8754dc96afa51a09bc4110e8ffe95d0b2b1c87be0e7f3cddada48dbf23c'
            'e4f3e62a0def31cb388f184a0df6bcbef3de99f4c09727820b0a78dc6392f73e')
validpgpkeys=('E0A3EB202F8E57528E13E72FD7574483BB57B18D'  # Jonathan Esk-Riddell <jr@jriddell.org>
              '0AAC775BB6437A8D9AF7A3ACFE0784117FBCE11D'  # Bhushan Shah <bshah@kde.org>
              'D07BD8662C56CB291B316EB2F5675605C74E02CF'  # David Edmundson <davidedmundson@kde.org>
              '1FA881591C26B276D7A5518EEAAF29B42A678C20') # Marco Martin <notmart@gmail.com>

prepare() {
  cd $pkgname-$pkgver
  patch -Np1 -i ../0001-launcher.socket-bump-feature-set-to-limit-activation.patch
  patch -Np1 -i ../0002-launcher.socket-attach-the-unit-to-plasma.patch
  patch -Np1 -i ../0003-launcher.service-ensure-it-doesn-t-participate-in-se.patch
  patch -Np1 -i ../0004-launcher.socket-correctly-change-wantedby.patch
  patch -Np1 -i ../0005-launcher.socket-loosen-grip-on-plasma-core.target.patch
  patch -Np1 -i ../0006-cleanup.timer-do-not-start-outside-plasma.patch
  patch -Np1 -i ../0007-postman.path-do-not-start-outside-plasma.patch
  patch -Np1 -i ../0008-coredump-don-t-process-crashes-of-our-own-binaries.patch
}

build() {
  cmake -B build  -S $pkgname-$pkgver \
    -DCMAKE_INSTALL_LIBEXECDIR=lib \
    -DBUILD_TESTING=OFF \
    -DWITH_PYTHON_VENDORING=OFF
  cmake --build build
}

package() {
  DESTDIR="$pkgdir" cmake --install build
}
