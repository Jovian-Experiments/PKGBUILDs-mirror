# Maintainer David Edmundson (bluesystems@davidedmundson.co.uk)

pkgname=steamdeck-kde-presets
_srctag=0.9
pkgver=${_srctag#jupiter-}
pkgrel=1
arch=('any')
url=""
pkgdesc="Steamdeck KDE Presets"
license=('GPL2')
makedepends=('git')
source=("git+ssh://git@gitlab.steamos.cloud/jupiter/steamdeck-kde-presets.git#tag=$_srctag")
sha512sums=(SKIP)

package() {
  cp -R "$srcdir"/steamdeck-kde-presets/* "$pkgdir"
}
