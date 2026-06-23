# Maintainer David Edmundson (bluesystems@davidedmundson.co.uk)

pkgname=steamdeck-kde-presets
_srctag=3.9.2
pkgver=${_srctag#jupiter-}
pkgrel=2
arch=('any')
url=""
pkgdesc="Steamdeck KDE Presets"
license=('GPL2')
depends=('kdialog')
optdepends=(
  'steamos-alias: for steamos-alias compatibility symlinks'
)
makedepends=('git' 'openssh')
source=("git+ssh://git@gitlab.steamos.cloud/jupiter/steamdeck-kde-presets.git#tag=$_srctag")
sha512sums=('652ae1f5632bebaa9c5191db751c8ef2bfd8f126be857dc1a0a165a7c1b24c9a3bdef858ebe6960081764a228baafc4a5b7c9a7293347ad23cd55017f1d53a0c')

package() {
  local aliased=
  cp -R "$srcdir"/steamdeck-kde-presets/* "$pkgdir"
  install -d -m0755 "$pkgdir/usr/lib/systemd/system/multi-user.target.wants/"
  ln -s ../steamos-set-plasma-theme.service "$pkgdir/usr/lib/systemd/system/multi-user.target.wants/"
}
