# Maintainer David Edmundson (bluesystems@davidedmundson.co.uk)

pkgname=steamdeck-kde-presets
_srctag=3.9.0
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
sha512sums=('81743bb8cdf1239b6be65a858321bec14eb48637dfccc6da8b97898fd4c6cc6cc790b5f8540242344f62da8a26aae3dea8138e5f1fe4ede11bc56f17d03df10d')

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
