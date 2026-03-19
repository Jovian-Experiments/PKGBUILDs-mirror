# Maintainer: Adam Weld <weld@valvesoftware.com>
# Maintainer: Christian Marcheselli <christianm@valvesoftware.com>

pkgname=jupiter-fan-control
_srctag=20260319.1
pkgver=${_srctag//-/.}
pkgrel=4
arch=('any')
license=('MIT')
pkgdesc="Jupiter fan controller"
url='https://gitlab.steamos.cloud/jupiter/jupiter-fan-control/-/tree/$_srctag'
depends=('python-pyaml' 'python>=3.13' 'python<3.14')
sha512sums=('d922a8409675f698ea811445f92341daca0dc8cadb411604fef899a223498fcad1c5f8723b1a55041d153bbb5374e96a1c26c147399c11765e67aa14d476da6b')
makedepends=('git' 'rsync' 'openssh')

source=("git+ssh://git@gitlab.steamos.cloud/jupiter/jupiter-fan-control.git#tag=$_srctag")

package() {
   rsync -a --exclude 'README.md' "$srcdir"/jupiter-fan-control/* "$pkgdir"
}
