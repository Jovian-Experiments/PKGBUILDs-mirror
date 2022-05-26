# Maintainer: John Schoenick <johns@valvesoftware.com>
# Maintainer: Levente Polyak <anthraxx[at]archlinux[dot]org>
# Maintainer: Giancarlo Razzolini <grazzolini@archlinux.org>
# Contributor: Daniel Wallace <danielwallace at gtmanfred dot com>
# Contributor: K900 <k0009000@gmail.com>

_basename=steam
pkgname=steam-jupiter-stable
pkgver=1.0.0.74
pkgrel=2.15
pkgdesc="Valve's digital software delivery system - Jupiter bootstrapped packaging"
url='https://steampowered.com/'
arch=('x86_64')
license=('custom')
depends=('bash' 'desktop-file-utils' 'diffutils' 'hicolor-icon-theme' 'curl' 'dbus'
         'freetype2' 'gdk-pixbuf2' 'ttf-font' 'zenity' 'lsb-release' 'nss' 'usbutils'
         'xorg-xrandr' 'vulkan-driver' 'vulkan-icd-loader' 'lsof' 'python')
depends_x86_64=('lib32-libgl' 'lib32-gcc-libs' 'lib32-libx11' 'lib32-libxss'
                'lib32-alsa-plugins' 'lib32-libgpg-error' 'lib32-fontconfig'
                'lib32-nss' 'lib32-vulkan-driver' 'lib32-vulkan-icd-loader'
                'lib32-pipewire')
provides=('steam')
conflicts=('steam')

# Jupiter: Drops native-runtime patches
# optdepends=('steam-native-runtime: steam native runtime support')

# Jupiter: Including fully bootstrapped steam image on expected branch
_fat_bootstrap=steam_jupiter_stable_bootstrapped_20220226.1.tar.xz
noextract=("$_fat_bootstrap")
source=(https://repo.steampowered.com/${_basename}/pool/${_basename}/s/${_basename}/${_basename}_${pkgver}{.tar.gz,.dsc}
        http://latest-pacman.internal.steamos.cloud/misc/steam-snapshots/"$_fat_bootstrap"
        70-steam-jupiter-input.rules
        steam-jupiter.sh
        steam-runtime.sh)
sha512sums=('2a08d9bb6e17a481c577b6aad7d53b51c7d9f6638aaccffc6b9f750dca4a1f9d12c02fd1446c174e979605ef29bdc10fc8249fd97fe79d62934efe26f4ac7369'
            '754161985b7a2dc5b10c06ec88f6a4eeef9b4dc0daddeb33c27d01a948223b3b2b17da6d14144f772f7b3156665b10543ad9a860b471c72e2d6bd543f143d964'
            'bc11f014e94670982d984779ef53ec917feea0c8300e5d77310befe5ec2933a8f7272b34534175eafd8523da10427b32fe90b0b0a43767f4a952378e6194d5ad'
            '85c66db5619fc70553fb4daa4bb9d7784f40586c771853d91147de99c48c58ac5727f2bae4e165a8fa898e9bcf4fb3bcce6c1409cc8edcf85a3965572456990d'
            '6c1b79bace3bd30f228a02072b9941c9b0fffb65bbd6c28c509025dbafc99c9c87272f62303e4704775ce304b4593ce8eaf9eb86bd2b957aef47fde33408299f'
            '5e75c019e9fe8c67d686c4e3343dac1180a69a4bdb7d39b333415c63201eef9b98da5619dbf6fd8daa6884e65bc7f8afc9e52778682425e5a75987d527eae6f0')
b2sums=('dbe02066d08530378ff922daf8733ad373c0eae9be94479aba94077a0f5c093afc39a95c6770494655af1c33895c981219418f8d4024c391a337d16ec32253c1'
        '3e82229128b10edf8d11a2130490e8f75b2ec91ccaf7e103d7c734b123791285c805bfb303aa374e04087ffdb501510eab9b2a02953e1ec78c656677786eeff9'
        'c04bde3686c022bcd31a69370db754761244be2c8c41418187860ed2e6c394a0851de79c07a280740ba78d00136249cf5cdd28baa209ce52dc75ecdce26e4200'
        '8ae0bfdf6bc62460a64d84acb3dbd5d95257749f2560938eefd68a58727f310c8450ce756ed938ebe46a3074860d1abdd744689caf9bde01c89ae02f8c63179e'
        'dff1dd0dea4b547427a02fb914ed0e7aaa8150daa130271106eeae596566d9fc1e868b8be2f37c1777dbffbd96634b0c862e86706cf77d1556f57aba7dda5cb1'
        'c6bac99336b7c30fec7cdbaf9e949555c687dd9dff50bcae136134d6314f4b841f5fc66ddb2caac1b003690b926fd4afbdc11da143b4674db4b75f27709fdd23')

validpgpkeys=('BA1816EF8E75005FCF5E27A1F24AEA9FB05498B7') # linux@steampowered.com

prepare() {
  cd ${_basename}-launcher

  # Jupiter
  # No preparation necessary
}

package() {
  cd ${_basename}-launcher
  make DESTDIR="${pkgdir}" install

  install -Dm 755 "${srcdir}/steam-runtime.sh" "${pkgdir}/usr/bin/steam-runtime"
  install -d "${pkgdir}/usr/lib/steam"
  mv "${pkgdir}/usr/bin/steam" "${pkgdir}/usr/lib/steam/steam"
  ln -sf /usr/bin/steam-runtime "${pkgdir}/usr/bin/steam"

  install -Dm 644 COPYING steam_subscriber_agreement.txt -t "${pkgdir}/usr/share/licenses/${pkgname}"
  install -Dm 644 debian/changelog -t "${pkgdir}/usr/share/doc/${pkgname}"

  # blank steamdeps because apt-get
  ln -sf /usr/bin/true "${pkgdir}/usr/bin/steamdeps"

  # Jupiter
  # Install permissive input rules
  install -Dm 644 "${srcdir}/70-steam-jupiter-input.rules" \
    "${pkgdir}/usr/lib/udev/rules.d/70-steam-jupiter-input.rules"

  # Jupiter
  # Replace the runtime with our own wrapper
  rm "${pkgdir}/usr/bin/steam-runtime"
  install -Dm 755 "${srcdir}/steam-jupiter.sh" "${pkgdir}/usr/bin/steam-jupiter"
  ln -sf /usr/bin/steam-jupiter "${pkgdir}/usr/bin/steam"

  # Replace bootstrapper with fat one
  rm "$pkgdir"/usr/lib/steam/bootstraplinux_ubuntu12_32.tar.xz
  install -Dm 644 "$srcdir/$_fat_bootstrap" "$pkgdir"/usr/lib/steam/bootstraplinux_ubuntu12_32.tar.xz
}

# vim: ts=2 sw=2 et:
