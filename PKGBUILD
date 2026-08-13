# Maintainer David Edmundson (bluesystems@davidedmundson.co.uk)

pkgname=steamdeck-kde-presets
_srctag=3.9.4
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
sha512sums=('7e0d49186a036ac2972b471e858ee1e0d7cc7897ad300f295a0645f9c741a1943a6d078c5becc4a66db75942283e43f42247ebf001d0b5bc7278c503158e7be3')

package() {
  local aliased=
  rm "$srcdir"/steamdeck-kde-presets/README.md
  cp -R "$srcdir"/steamdeck-kde-presets/* "$pkgdir"
  install -d -m0755 "$pkgdir/usr/lib/systemd/system/multi-user.target.wants/"
  ln -s ../steamos-set-plasma-theme.service "$pkgdir/usr/lib/systemd/system/multi-user.target.wants/"
}
