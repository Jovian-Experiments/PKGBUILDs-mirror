# Maintainer: Felix Yan <felixonmars@archlinux.org>
# Maintainer: Antonio Rojas <arojas@archlinux.org>
# Contributor: Andrea Scarpino <andrea@archlinux.org>

pkgname=konsole
pkgver=24.12.0
pkgrel=1
arch=(x86_64)
url='https://apps.kde.org/konsole/'
pkgdesc='KDE terminal emulator'
license=(GPL-2.0-or-later
         LGPL-2.0-or-later)
groups=(kde-applications
        kde-utilities)
depends=(glibc
         gcc-libs
         icu
         kbookmarks
         kcolorscheme
         kconfig
         kconfigwidgets
         kcoreaddons
         kcrash
         kdbusaddons
         kglobalaccel
         kguiaddons
         ki18n
         kiconthemes
         kio
         knewstuff
         knotifications
         knotifyconfig
         kparts
         kpty
         kservice
         ktextwidgets
         kwidgetsaddons
         kwindowsystem
         kxmlgui
         qt6-base
         qt6-multimedia
         sh)
makedepends=(extra-cmake-modules
             kdoctools)
optdepends=('keditbookmarks: to manage bookmarks')
source=(https://download.kde.org/stable/release-service/$pkgver/src/$pkgname-$pkgver.tar.xz{,.sig}
        0001-Clear-arguments-if-command-not-found.patch # Security fix, can be dropped on upgrade to 25.04.1 or newer
)
sha256sums=('255f344d6ffe338dfeafd610bf6d63ed1bf9adf306948d58351838c057b21a54'
            'SKIP'
            '2901bd15f799d77c2b7fe5ae3553bd44fa06160c7c2508b7ce3cd4982bd0e561')
validpgpkeys=(CA262C6C83DE4D2FB28A332A3A6A4DB839EAA6D7  # Albert Astals Cid <aacid@kde.org>
              F23275E4BF10AFC1DF6914A6DBD2CE893E2D1C87  # Christoph Feck <cfeck@kde.org>
              D81C0CB38EB725EF6691C385BB463350D6EF31EF) # Heiko Becker <heiko.becker@kde.org>

prepare() {
  patch -p1 -d "$srcdir/$pkgname-$pkgver" -i "$srcdir/0001-Clear-arguments-if-command-not-found.patch"
}


build() {
  cmake -B build -S $pkgname-$pkgver \
    -DBUILD_TESTING=OFF
  cmake --build build
}

package() {
  DESTDIR="$pkgdir" cmake --install build
}
