# Maintainer David Edmundson (bluesystems@davidedmundson.co.uk)

pkgname=steamdeck-kde-presets
_srctag=3.8.1
pkgver=${_srctag#jupiter-}
pkgrel=1
arch=('any')
url=""
pkgdesc="Steamdeck KDE Presets"
license=('GPL2')
depends=('kdialog')
makedepends=('git' 'openssh')
source=("git+ssh://git@gitlab.steamos.cloud/jupiter/steamdeck-kde-presets.git#tag=$_srctag")
sha512sums=('7be34248e2b072cd5477cf86e6b7492317fd658cde76d06e60030766683cb603072c17f2f15d5486c2e13d1a888ec28c64b53f1bd98c18a7d967dc3c3bda8cd8')

package() {
  cp -R "$srcdir"/steamdeck-kde-presets/* "$pkgdir"
  install -d -m0755 "$pkgdir/usr/lib/systemd/system/multi-user.target.wants/"
  ln -s ../steamos-set-plasma-theme.service "$pkgdir/usr/lib/systemd/system/multi-user.target.wants/"
}
