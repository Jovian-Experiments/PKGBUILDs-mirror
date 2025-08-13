# Maintainer David Edmundson (bluesystems@davidedmundson.co.uk)

pkgname=steamdeck-kde-presets
_srctag=3.7.0
pkgver=${_srctag#jupiter-}
pkgrel=1
arch=('any')
url=""
pkgdesc="Steamdeck KDE Presets"
license=('GPL2')
depends=('kdialog')
makedepends=('git' 'openssh')
source=("git+ssh://git@gitlab.steamos.cloud/jupiter/steamdeck-kde-presets.git#tag=$_srctag")
sha512sums=('2f095e8d6cec42587ef40f8e01a86b09a5c2be016fd0e7406f7b9e84784419ed8cfdcc339ee4fd62e624fa30426ce9a9ddba52940665206159c3765a2e5f909b')

package() {
  cp -R "$srcdir"/steamdeck-kde-presets/* "$pkgdir"
  install -d -m0755 "$pkgdir/usr/lib/systemd/system/multi-user.target.wants/"
  ln -s ../steamos-set-plasma-theme.service "$pkgdir/usr/lib/systemd/system/multi-user.target.wants/"
}
