# Maintainer David Edmundson (bluesystems@davidedmundson.co.uk)

pkgname=steamdeck-kde-presets
_srctag=3.9.3
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
sha512sums=('595b493fcceb489a2fa66f4bb5b21c5cfdad0392cb675bcfd7a3f85e3f92347556a01bb8f7e441b76859c614c96c4347358bc9cab2650d705e3ae21796fcab47')

package() {
  local aliased=
  cp -R "$srcdir"/steamdeck-kde-presets/* "$pkgdir"
  install -d -m0755 "$pkgdir/usr/lib/systemd/system/multi-user.target.wants/"
  ln -s ../steamos-set-plasma-theme.service "$pkgdir/usr/lib/systemd/system/multi-user.target.wants/"
}
