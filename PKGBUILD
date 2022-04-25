# Maintainer: Adam Weld <weld@valvesoftware.com>
# Maintainer: Christian Marcheselli <christianm@valvesoftware.com>

pkgname=jupiter-fan-control
_srctag=20220421.2
pkgver=${_srctag//-/.}
pkgrel=1
arch=('any')
license=('MIT')
pkgdesc="Jupiter fan controller"
url='https://gitlab.steamos.cloud/jupiter/jupiter-fan-control/-/tree/$_srctag'
depends=('python3' 'python-pyaml')
sha512sums=(SKIP)
makedepends=('git' 'rsync')

source=("git+ssh://git@gitlab.internal.steamos.cloud/jupiter/jupiter-fan-control.git#tag=$_srctag")

package() {
   rsync -a --exclude 'README.md' "$srcdir"/jupiter-fan-control/* "$pkgdir"
}
