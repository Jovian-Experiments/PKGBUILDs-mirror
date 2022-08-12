# Maintainer: John Schoenick <johns@valvesoftware.com>
# Maintainer: Levente Polyak <anthraxx[at]archlinux[dot]org>
# Maintainer: Giancarlo Razzolini <grazzolini@archlinux.org>
# Contributor: Daniel Wallace <danielwallace at gtmanfred dot com>
# Contributor: K900 <k0009000@gmail.com>

_basename=steam
pkgname=steam-jupiter-oobe
pkgver=1.0.0.74
# based on upstream steam 1.0.0.74-2, based on steam-jupiter-stable rel 2.19.  Really overloading pkgrel's meaning here.
pkgrel=2.1902
pkgdesc="Valve's digital software delivery system - Jupiter bootstrapped packaging"
url='https://steampowered.com/'
arch=('x86_64')
license=('custom')
depends=('bash' 'desktop-file-utils' 'diffutils' 'hicolor-icon-theme' 'curl' 'dbus'
         'freetype2' 'gdk-pixbuf2' 'ttf-font' 'zenity' 'lsb-release' 'nss' 'usbutils'
         'xorg-xrandr' 'vulkan-driver' 'vulkan-icd-loader' 'lsof' 'python')
# lib32-pipewire: https://bugs.archlinux.org/task/75155
# lib32-fontconfig: https://bugs.archlinux.org/task/74827
# lib32-systemd, lib32-libxinerama: https://bugs.archlinux.org/task/75156
# lib32-libnm, lib32-libva:  https://bugs.archlinux.org/task/75157
depends_x86_64=('lib32-libgl' 'lib32-gcc-libs' 'lib32-libx11' 'lib32-libxss'
                'lib32-alsa-plugins' 'lib32-libgpg-error' 'lib32-fontconfig'
                'lib32-nss' 'lib32-vulkan-driver' 'lib32-vulkan-icd-loader'
                'lib32-pipewire' 'lib32-systemd' 'lib32-libxinerama' 'lib32-libva')
provides=('steam')
conflicts=('steam')

# Jupiter: Drops native-runtime patches
# optdepends=('steam-native-runtime: steam native runtime support')
optdepends=('lib32-libnm: integration with networkmanager')

# Jupiter: Including fully bootstrapped steam image on expected branch
_fat_bootstrap=steam_jupiter_goldmaster_bootstrapped_20220812.tar.xz
noextract=("$_fat_bootstrap")
source=(https://repo.steampowered.com/${_basename}/pool/${_basename}/s/${_basename}/${_basename}_${pkgver}{.tar.gz,.dsc}
        http://latest-pacman.internal.steamos.cloud/misc/steam-snapshots/"$_fat_bootstrap"
        70-steam-jupiter-input.rules
        steam-jupiter.sh
        steam-runtime.sh)
sha512sums=('2a08d9bb6e17a481c577b6aad7d53b51c7d9f6638aaccffc6b9f750dca4a1f9d12c02fd1446c174e979605ef29bdc10fc8249fd97fe79d62934efe26f4ac7369'
            '754161985b7a2dc5b10c06ec88f6a4eeef9b4dc0daddeb33c27d01a948223b3b2b17da6d14144f772f7b3156665b10543ad9a860b471c72e2d6bd543f143d964'
            'dc92b8c0f1708ecb5049274715d04956bb5b561208174d0c487975b6eeea12df2a0f1937fc71f4d3d5ea576127c1422b7bdd9caee094f8c439b01eb2e7fea8fe'
            '85c66db5619fc70553fb4daa4bb9d7784f40586c771853d91147de99c48c58ac5727f2bae4e165a8fa898e9bcf4fb3bcce6c1409cc8edcf85a3965572456990d'
            'da89061db6d4bf61b395339442483570c0c9c5889d609d9d84aed07d8e7995621929e3c82450059304a770f6429744dce68b0d939dc4ebe5b6b1c5d4eed33b62'
            '5e75c019e9fe8c67d686c4e3343dac1180a69a4bdb7d39b333415c63201eef9b98da5619dbf6fd8daa6884e65bc7f8afc9e52778682425e5a75987d527eae6f0')
b2sums=('dbe02066d08530378ff922daf8733ad373c0eae9be94479aba94077a0f5c093afc39a95c6770494655af1c33895c981219418f8d4024c391a337d16ec32253c1'
        '3e82229128b10edf8d11a2130490e8f75b2ec91ccaf7e103d7c734b123791285c805bfb303aa374e04087ffdb501510eab9b2a02953e1ec78c656677786eeff9'
        '20877f768aa963683142e42f078b82648c8b08566d719d0fa211f86e616829b5bf2ac20c7e3b067c562db12b114bd7d7f30a866718be05f981b7ea56e47a7d38'
        '8ae0bfdf6bc62460a64d84acb3dbd5d95257749f2560938eefd68a58727f310c8450ce756ed938ebe46a3074860d1abdd744689caf9bde01c89ae02f8c63179e'
        'bc9998406c08107e5a1f3d8cb3f2bd8f568c86af0841408244bc3b28c5a6cb78b6ac9aa6fb6ea05decb7894bb68d0c28f10b438a2a7bc58fd57780c40f4b22f1'
        'c6bac99336b7c30fec7cdbaf9e949555c687dd9dff50bcae136134d6314f4b841f5fc66ddb2caac1b003690b926fd4afbdc11da143b4674db4b75f27709fdd23')

validpgpkeys=('BA1816EF8E75005FCF5E27A1F24AEA9FB05498B7') # linux@steampowered.com

prepare() {
  cd ${_basename}-launcher
  # Drop: https://bugs.archlinux.org/task/75143
  # apply roundups for udev rules
  sed -r 's|("0666")|"0660", TAG+="uaccess"|g' -i subprojects/steam-devices/60-steam-input.rules
  sed -r 's|("misc")|\1, OPTIONS+="static_node=uinput"|g' -i subprojects/steam-devices/60-steam-input.rules
  sed -r 's|(, TAG\+="uaccess")|, MODE="0660"\1|g' -i subprojects/steam-devices/60-steam-vr.rules

  # Drop: https://bugs.archlinux.org/task/75145
  # Jupiter: No please
  # separated runtime/native desktop files
  #   sed -r 's|(Name=Steam)|\1 (Runtime)|' -i steam.desktop
  #   sed -r 's|(/usr/bin/steam)|\1-runtime|' -i steam.desktop
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
