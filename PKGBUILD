# Maintainer: John Schoenick <johns@valvesoftware.com>
# Maintainer: Levente Polyak <anthraxx[at]archlinux[dot]org>
# Maintainer: Giancarlo Razzolini <grazzolini@archlinux.org>
# Contributor: Daniel Wallace <danielwallace at gtmanfred dot com>
# Contributor: K900 <k0009000@gmail.com>

_basename=steam
pkgname=steam-jupiter-stable
pkgver=1.0.0.79
pkgrel=1.2
pkgdesc="Valve's digital software delivery system - Jupiter bootstrapped packaging"
url='https://steampowered.com/'
arch=('x86_64')
license=('custom')
# libxcrypt-compat, lib32-libxcrypt-compat: https://bugs.archlinux.org/task/75443
depends=(
  bash
  desktop-file-utils
  diffutils
  hicolor-icon-theme
  curl
  dbus
  freetype2
  gdk-pixbuf2
  ttf-font
  zenity
  lsb-release
  nss
  usbutils
  xorg-xrandr
  vulkan-driver
  vulkan-icd-loader
  lsof
  python
  libxcrypt-compat
)
# lib32-pipewire: https://gitlab.archlinux.org/archlinux/packaging/packages/steam/-/issues/9
# lib32-fontconfig: https://gitlab.archlinux.org/archlinux/packaging/packages/steam/-/issues/6
# lib32-systemd, lib32-libxinerama: https://gitlab.archlinux.org/archlinux/packaging/packages/steam/-/issues/10
# lib32-libnm, lib32-libva: https://gitlab.archlinux.org/archlinux/packaging/packages/steam/-/issues/11
depends_x86_64=(
  lib32-libxcrypt-compat
  lib32-libgl
  lib32-gcc-libs
  lib32-libx11
  lib32-libxss
  lib32-alsa-plugins
  lib32-libgpg-error
  lib32-fontconfig
  lib32-nss
  lib32-vulkan-driver
  lib32-vulkan-icd-loader
  lib32-pipewire
  lib32-systemd
  lib32-libxinerama
  lib32-libva
)
provides=('steam')
conflicts=('steam')

# Jupiter: Drops native-runtime patches
# optdepends=('steam-native-runtime: steam native runtime support')
optdepends=('lib32-libnm: integration with networkmanager')

# Jupiter: Including fully bootstrapped steam image on expected branch
_fat_bootstrap=steam_jupiter_stable_bootstrapped_20240509.1.tar.xz
noextract=("$_fat_bootstrap")
source=(https://repo.steampowered.com/${_basename}/archive/beta/${_basename}_${pkgver}{.tar.gz,.dsc}
        http://latest-pacman.internal.steamos.cloud/misc/steam-snapshots/"$_fat_bootstrap"
        70-steam-jupiter-input.rules
        steam-jupiter.sh
        steam-runtime.sh
        # Remove when we go to 1.0.0.81 (https://gitlab.steamos.cloud/holo-team/tasks/-/issues/1398)
        bin_steam.sh
        )
sha512sums=('52d1a23f43012af641ebc9a03a444b6944ea966e0814619c890e792442e760a96bf570a84e4f8b38552904dafb6572a92de31154ddefe1eb8d702106605c8497'
            '68b59c7b4e9d55b60f92b466e01c10b5d84309e5822adb6bfdee8790a77357eb513166d958f25fc8f17f4f786b2dae19f281c330ff7bc34d4dbb17a4b263c99a'
            'ba46762da3a809735e57c84afea525f703e6a5c67d2ab14e2dde949f2fdb490f198eb147deb5297349a788e5645949490574175935e66dfe11b6f9d4069140cc'
            '85c66db5619fc70553fb4daa4bb9d7784f40586c771853d91147de99c48c58ac5727f2bae4e165a8fa898e9bcf4fb3bcce6c1409cc8edcf85a3965572456990d'
            '7d568c24f46902715c08797fc1148cfab9ee924d49c9bcd97cd1bd4106dfdd35409912ca1b598f50a50c62394f9618b595ca5bafdc4b9ee3b013398826cc4b01'
            '5e75c019e9fe8c67d686c4e3343dac1180a69a4bdb7d39b333415c63201eef9b98da5619dbf6fd8daa6884e65bc7f8afc9e52778682425e5a75987d527eae6f0'
            '47e2b8d2ecdb40ef2d5555e31122f1e863920998089f9dc7ce58b112ba72df6745ae30927ef158cfa735faad41b82bd6cdf25e9c69d7e780374648f57bdc3b72')
b2sums=('73538d120182b37cca15e99512af6c689ff29e47cd37ea5bdd0d754f42aacd69aa71125e3c07140d8b8eaf55ee980babdfa6f7a1de8daf8c6ce8af4b03608cbc'
        '27f2df8198d0fcf5173f3b4e3cef38d9cfc122aa4e5383ee5924597892137918cbcf5fce813f6379412b5a61c676b13f85ef70798ab94a91d67eaaf8583b7250'
        'be826a4abea8acbeca1a3ac3037db3dfa7f997669de409a13dc3db3040b7fcab72b77b46942d29553bfcf017d1b04ee4e09f5193b26afcd63373130386cedd32'
        '8ae0bfdf6bc62460a64d84acb3dbd5d95257749f2560938eefd68a58727f310c8450ce756ed938ebe46a3074860d1abdd744689caf9bde01c89ae02f8c63179e'
        '987eeed26caf80e31ce289116f7d2fc7742949a6b5681005c0257a0fa490bb0bbbdde5ab1ec4794732bf58a22cabe9859c4c6a0f19b8be8aa97b5df659304657'
        'c6bac99336b7c30fec7cdbaf9e949555c687dd9dff50bcae136134d6314f4b841f5fc66ddb2caac1b003690b926fd4afbdc11da143b4674db4b75f27709fdd23'
        'fb6df965a9e537835262a2e0e722469799d72b2a7afa1793efa69685a60dfb8624e25f9dced7dcde2549eb4c2a37fc588593e6182c83a77956e4263e0c87853e')

validpgpkeys=('BA1816EF8E75005FCF5E27A1F24AEA9FB05498B7') # linux@steampowered.com

prepare() {
  cd ${_basename}-launcher
  # Drop: https://gitlab.archlinux.org/archlinux/packaging/packages/steam/-/issues/7
  # apply roundups for udev rules
  sed -r 's|("0666")|"0660", TAG+="uaccess"|g' -i subprojects/steam-devices/60-steam-input.rules
  sed -r 's|("misc")|\1, OPTIONS+="static_node=uinput"|g' -i subprojects/steam-devices/60-steam-input.rules
  sed -r 's|(, TAG\+="uaccess")|, MODE="0660"\1|g' -i subprojects/steam-devices/60-steam-vr.rules

  # Drop: https://gitlab.archlinux.org/archlinux/packaging/packages/steam/-/issues/8
  # Jupiter: No please
  # separated runtime/native desktop files
  #   sed -r 's|(Name=Steam)|\1 (Runtime)|' -i steam.desktop
  #   sed -r 's|(/usr/bin/steam)|\1-runtime|' -i steam.desktop
}

package() {
  # Remove when we go to 1.0.0.81 (https://gitlab.steamos.cloud/holo-team/tasks/-/issues/1398)
  cp bin_steam.sh ${_basename}-launcher

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
