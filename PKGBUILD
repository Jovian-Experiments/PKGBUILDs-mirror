# Maintainer David Edmundson (bluesystems@davidedmundson.co.uk)

pkgname=steamdeck-kde-presets
_srctag=3.8.3
pkgver=${_srctag#jupiter-}
pkgrel=1
arch=('any')
url=""
pkgdesc="Steamdeck KDE Presets"
license=('GPL2')
depends=('kdialog')
makedepends=('git' 'openssh')
source=("git+ssh://git@gitlab.steamos.cloud/jupiter/steamdeck-kde-presets.git#tag=$_srctag")
sha512sums=('191d6e492f91fdf1cd53c3eb4e453b3a24fcc9b2497a4dcec78046d287a73e9c947cddf81c265c40e031655020d5af4e81c90f75ea2ee218e9b099c0cf969c82')

package() {
  cp -R "$srcdir"/steamdeck-kde-presets/* "$pkgdir"
  install -d -m0755 "$pkgdir/usr/lib/systemd/system/multi-user.target.wants/"
  ln -s ../steamos-set-plasma-theme.service "$pkgdir/usr/lib/systemd/system/multi-user.target.wants/"
}
