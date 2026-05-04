# Maintainer David Edmundson (bluesystems@davidedmundson.co.uk)

pkgname=steamdeck-kde-presets
_srctag=3.9.1
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
sha512sums=('0ad9c29baf6d8f513f3a4337d2e7c59d352a661c277962b6b93f47f61bbcd17ffb59f2b2d86b3e6f8cee53e2a55cc87a1b1f28fc067db2dae5b4eb91a9f3a99d')

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
