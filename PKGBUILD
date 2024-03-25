# Maintainer: Emil Velikov <emil.l.velikov@gmail.com>

pkgname=holo-keyring
_srctag=holo-20240322-sq033
pkgver=${_srctag#holo-}
pkgver=${pkgver//-/.}
pkgrel=1
pkgdesc='Holo PGP keyring'
arch=(any)
url='https://gitlab.steamos.cloud/holo/archlinux-keyring/'
license=(GPL)
groups=(holo-base)
install=$pkgname.install
makedepends=('git' 'python' 'sequoia-sq>=0.33' 'sequoia-sq<0.34')
source=("$pkgname-$pkgver::git+https://gitlab.steamos.cloud/holo/archlinux-keyring#tag=$_srctag")
sha256sums=('SKIP')

package() {
  cd $pkgname-$pkgver
  make PREFIX=/usr DESTDIR="$pkgdir" install
}
