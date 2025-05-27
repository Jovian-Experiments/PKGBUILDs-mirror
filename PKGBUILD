# Maintainer David Edmundson (bluesystems@davidedmundson.co.uk)

pkgname=steamdeck-kde-presets
_srctag=0.30
pkgver=${_srctag#jupiter-}
pkgrel=1
arch=('any')
url=""
pkgdesc="Steamdeck KDE Presets"
license=('GPL2')
depends=('kdialog')
makedepends=('git' 'openssh')
source=("git+ssh://git@gitlab.steamos.cloud/jupiter/steamdeck-kde-presets.git#tag=$_srctag")
sha512sums=('4506aee368e06dfd10a754097fa113ae43be99433871c4510a9b6b753b363f731dac86caf463ca04da5acd7f17f748ee330a2a870588c47f522efac04777087d')

package() {
  cp -R "$srcdir"/steamdeck-kde-presets/* "$pkgdir"
  install -d -m0755 "$pkgdir/usr/lib/systemd/system/multi-user.target.wants/"
  ln -s ../steamos-set-plasma-theme.service "$pkgdir/usr/lib/systemd/system/multi-user.target.wants/"
}
