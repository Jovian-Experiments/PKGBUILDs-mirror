# Maintainer: Emil Velikov <emil.l.velikov@gmail.com>

pkgname=holo-keyring
pkgver=20220203
_srctag=holo-${pkgver}
# TODO: figure out the proper URL and use the signed tag directly
_commit=baeb322ec276a184e7107b1ba509a3f92c0ec668 # tags/$_srctag^0
pkgrel=5
pkgdesc='Holo PGP keyring'
arch=(any)
url='https://gitlab.steamos.cloud/holo/archlinux-keyring/'
license=(GPL)
groups=(holo-base)
install=$pkgname.install
makedepends=('git' 'openssh' 'python' 'sequoia-sq')
source=("$pkgname-$pkgver::git+https://gitlab.steamos.cloud/holo/archlinux-keyring#commit=$_commit")
sha256sums=('SKIP')
#validpgpkeys=('8703B6700E7EE06D7A39B8D6EDAE37B02CEB490D')  # Emil Velikov <emil.l.velikov@gmail.com>

package() {
  cd $pkgname-$pkgver
  make PREFIX=/usr DESTDIR="$pkgdir" install
}
