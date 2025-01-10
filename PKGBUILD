# Maintainer: Felix Yan <felixonmars@archlinux.org>
# Contributor: Rainy <rainylau(at)gmail(dot)com>
# Contributor: Lee.MaRS <leemars at gmail dot com>
# Contributor: Daniel J Griffiths <ghost1227@archlinux.us>

pkgname=ibus-anthy
pkgver=1.5.14
_commit=0962741856498bc9d197be0713b2fae1879c29ba  # Valve specific changes not yet upstream
pkgrel=4.3
pkgdesc='Japanese input method Anthy IMEngine for IBus Framework'
arch=('x86_64')
license=('LGPL')
url='https://github.com/ibus/ibus-anthy'
depends=('ibus' 'anthy' 'python>=3.13' 'python<3.14' 'gtk-update-icon-cache' 'python-gobject')
makedepends=('intltool' 'gobject-introspection' 'git')
source=("git+https://github.com/bjj/ibus-anthy.git#commit=$_commit")
sha512sums=('SKIP')

prepare() {
  cd $pkgname
  NOCONFIGURE=1 ./autogen.sh
}

build() {
  cd $pkgname

  ./configure --prefix=/usr --libexec=/usr/lib/ibus
  make
}

package() {
  cd $pkgname
  make DESTDIR="$pkgdir" install
}
