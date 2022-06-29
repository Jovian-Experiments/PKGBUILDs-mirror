# Maintainer: ghgh

pkgname=jupiter-validation-tools
_tag=jupiter-20220629.1
_tagstrip=${_tag#jupiter-}
pkgver=${_tagstrip//-/.}
pkgrel=2
arch=('any')
url="https://gitlab.steamos.cloud/Plagman/jupiter-validation-tools"
pkgdesc="Jupiter validation tools"
license=('MIT')
depends=('python-hid')
makedepends=('git')
source=("git+ssh://git@gitlab.internal.steamos.cloud/jupiter/jupiter-validation-tools.git#tag=$_tag")
sha512sums=(SKIP)

package() {
   mkdir -p $pkgdir/usr/share/jupiter-validation-tools
   cp -rv $srcdir/jupiter-validation-tools/* $pkgdir/usr/share/jupiter-validation-tools/
}
