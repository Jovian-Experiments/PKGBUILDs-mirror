# Maintainer David Edmundson (bluesystems@davidedmundson.co.uk)

pkgname=steamdeck-kde-presets
_srctag=3.8.4
pkgver=${_srctag#jupiter-}
pkgrel=1
arch=('any')
url=""
pkgdesc="Steamdeck KDE Presets"
license=('GPL2')
depends=('kdialog')
optdepends=(
  'steamos-customizations-jupiter: for holo-alias compatibility symlinks'
)
makedepends=('git' 'openssh')
_aliases=(/usr/bin/holo-{add-to-steam,nested-desktop,setup-kwallet} \
          /usr/lib/holo/holo-rotate-x11-screen)
source=("git+ssh://git@gitlab.steamos.cloud/jupiter/steamdeck-kde-presets.git#tag=$_srctag")
sha512sums=('1ca497aa9476d34b5e606970b708076c59d06ac695d5e8525c068d84d9b83677d7a843bcce5a73efebfd20b6ffc5633dea7cababa1e959a7371594b93b752523')

_make_steamos_alias ()
{
    local new="$1"
    local old="${new//holo/steamos}"
    local dir=$(dirname "$old")

    install -d -m0755 "$pkgdir"/"$dir"
    ln -sf "/usr/bin/holo-alias" "$pkgdir"/"$old"
}

package() {
  local aliased=
  cp -R "$srcdir"/steamdeck-kde-presets/* "$pkgdir"
  install -d -m0755 "$pkgdir/usr/lib/systemd/system/multi-user.target.wants/"
  ln -s ../steamos-set-plasma-theme.service "$pkgdir/usr/lib/systemd/system/multi-user.target.wants/"

  for aliased in "${_aliases[@]}"
  do
      _make_steamos_alias "$aliased"
  done
}
