# Maintainer: Felix Yan <felixonmars@archlinux.org>
# Contributor: Deon Spengler <deon@spengler.co.za>

pkgname=ddcutil
pkgver=2.1.4
pkgrel=1.1
pkgdesc='Query and change Linux monitor settings using DDC/CI and USB.'
url='http://ddcutil.com/'
arch=('x86_64')
license=('GPL2')
depends=('glib2' 'i2c-tools' 'libusb' 'libdrm' 'jansson')
makedepends=('systemd')
source=(https://github.com/rockowitz/ddcutil/archive/v$pkgver/$pkgname-$pkgver.tar.gz)
sha512sums=('8c352bfacc2a5cdd22b8d84f2facd58de6d425d0d3f98de543cf36a3e6b15aa10fc86e87780c82f872f0bf0db984e1cc800aaff914bafe4dbf17602e2a7caeb0')

prepare() {
  cd $pkgname-$pkgver
  NOCONFIGURE=1 ./autogen.sh
}

build() {
  cd $pkgname-$pkgver
  ./configure --prefix=/usr
  make
}

package() {
  cd $pkgname-$pkgver
  make DESTDIR="$pkgdir" install
  ############################################################################
  # SteamOS
  echo Remove udev rule to suppress controller firmware update screen blanking
  rm -v "$pkgdir"/usr/lib/udev/rules.d/60-ddcutil-usb.rules
  ############################################################################
}

# vim: ft=sh ts=2 sw=2 et
