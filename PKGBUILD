# Maintainer: Felix Yan <felixonmars@archlinux.org>
# Contributor: Rainy <rainylau(at)gmail(dot)com>
# Contributor: Lee.MaRS <leemars at gmail dot com>
# Contributor: Daniel J Griffiths <ghost1227@archlinux.us>

pkgname=ibus-anthy
pkgver=1.5.14
_commit=5ab156d8a54edd220473435bfe8af9c44e986ea8  # Valve specific changes not yet upstream
pkgrel=3
pkgdesc='Japanese input method Anthy IMEngine for IBus Framework'
arch=('x86_64')
license=('LGPL')
url='https://github.com/ibus/ibus-anthy'
depends=('ibus' 'anthy' 'python' 'gtk-update-icon-cache' 'python-gobject')
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
