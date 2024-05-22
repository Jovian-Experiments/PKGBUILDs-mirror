# Maintainer: Collabora Ltd <arnaud.ferraris@collabora.com>

pkgname=calamares-settings-steamos-git
pkgver=r323.d0d0ce2
pkgrel=3.1
pkgdesc='SteamOS theme and settings for the Calamares Installer'
arch=('any')
url=""
license=('custom:ISC')
depends=('calamares' 'python>=3.11' 'python<3.12' 'hicolor-icon-theme'
         'efibootmgr' # for the bootsetup
        )
makedepends=('git')
provides=("${pkgname%-git}")
conflicts=("${pkgname%-git}")
install="${pkgname%-git}.install"
source=("${pkgname%-git}::git+https://gitlab.steamos.cloud/holo/${pkgname%-git}.git#commit=d0d0ce2")
md5sums=('SKIP')

pkgver() {
    cd "${pkgname%-git}"
    printf "r%s.%s" "$(git rev-list --count HEAD)" "$(git rev-parse --short HEAD)"
}

package() {
    cd "${pkgname%-git}"

    install -Dm 0644 -t "$pkgdir/usr/share/icons/hicolor/256x256/apps/" "artwork/steamos-install.png"
    install -Dm 0755 -t "$pkgdir/usr/bin/" "steamos-install" "steamos-initial-setup" "steamos-uninstall"
    install -Dm 0644 -t "$pkgdir/usr/share/applications/" "steamos-install.desktop" "steamos-install-devel.desktop"
    install -Dm 0644 -t "$pkgdir/usr/share/calamares-steamos/" "steamos-initial-setup.desktop" "calamares-initial-setup.conf" "kwinrulesrc"
    install -Dm 0644 -t "$pkgdir/usr/share/bash-completion/completions/" "bash-completion/steamos-initial-setup" "bash-completion/steamos-install" "bash-completion/steamos-uninstall"

    install -Dm 0644 -t "$pkgdir/usr/share/licenses/${pkgname%-git}/" "COPYING"

    mkdir -p "$pkgdir/usr/share/calamares-steamos"
    cp -dR "settings/branding" "settings/steamos-initial-setup" "settings/steamos-install" "$pkgdir/usr/share/calamares-steamos"

    mkdir -p "$pkgdir/usr/lib/calamares-steamos"
    cp -dR "modules" "$pkgdir/usr/lib/calamares-steamos"
}
