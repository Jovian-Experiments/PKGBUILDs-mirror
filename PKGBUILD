# Maintainer: John Schoenick <johns@valvesoftware.com>
# Maintainer: Levente Polyak <anthraxx[at]archlinux[dot]org>
# Maintainer: Giancarlo Razzolini <grazzolini@archlinux.org>
# Contributor: Daniel Wallace <danielwallace at gtmanfred dot com>
# Contributor: K900 <k0009000@gmail.com>

_basename=steam
pkgname=steam-jupiter-stable
pkgver=1.0.0.78
pkgrel=1.2
pkgdesc="Valve's digital software delivery system - Jupiter bootstrapped packaging"
url='https://steampowered.com/'
arch=('x86_64')
license=('custom')
# libxcrypt-compat, lib32-libxcrypt-compat: https://bugs.archlinux.org/task/75443
depends=('bash' 'desktop-file-utils' 'diffutils' 'hicolor-icon-theme' 'curl' 'dbus'
         'libxcrypt-compat'
         'freetype2' 'gdk-pixbuf2' 'ttf-font' 'zenity' 'lsb-release' 'nss' 'usbutils'
         'xorg-xrandr' 'vulkan-driver' 'vulkan-icd-loader' 'lsof' 'python')
# lib32-pipewire: https://bugs.archlinux.org/task/75155
# lib32-fontconfig: https://bugs.archlinux.org/task/74827
# lib32-systemd, lib32-libxinerama: https://bugs.archlinux.org/task/75156
# lib32-libnm, lib32-libva:  https://bugs.archlinux.org/task/75157
depends_x86_64=('lib32-libgl' 'lib32-gcc-libs' 'lib32-libx11' 'lib32-libxss'
                'lib32-libxcrypt-compat'
                'lib32-alsa-plugins' 'lib32-libgpg-error' 'lib32-fontconfig'
                'lib32-nss' 'lib32-vulkan-driver' 'lib32-vulkan-icd-loader'
                'lib32-pipewire' 'lib32-systemd' 'lib32-libxinerama' 'lib32-libva')
provides=('steam')
conflicts=('steam')

# Jupiter: Drops native-runtime patches
# optdepends=('steam-native-runtime: steam native runtime support')
optdepends=('lib32-libnm: integration with networkmanager')

# Jupiter: Including fully bootstrapped steam image on expected branch
_fat_bootstrap=steam_jupiter_stable_bootstrapped_20231122.1.tar.xz
noextract=("$_fat_bootstrap")
source=(https://repo.steampowered.com/${_basename}/pool/${_basename}/s/${_basename}/${_basename}_${pkgver}{.tar.gz,.dsc}
        http://latest-pacman.internal.steamos.cloud/misc/steam-snapshots/"$_fat_bootstrap"
        70-steam-jupiter-input.rules
        steam-jupiter.sh
        steam-runtime.sh)
sha512sums=('3cebb97bff58d8b6a9aa7e7127873a2290056db107c3a02a2c8e030b9ce3ef9ceb94c2f81eb7fb423b9afce50244646bbc0707d515217d1c5455ba8aa05562ca'
            'de653b037717dc457aacf8f683bde7ac4542ced90d53349a8140bcda8d0f990a914d56655b73013f465e1fd41ad10a5330ef764087740b6dad55cd7ca5a41cbf'
            '17b7011fe7ae13834aa1f722724abfc3829ef8632bbabec2ae6b53ef0a9b6f1fc4db61b32056c62401e5aeb001e0f00d9e20f8ea045347b91cbe84ad4d0a919b'
            '85c66db5619fc70553fb4daa4bb9d7784f40586c771853d91147de99c48c58ac5727f2bae4e165a8fa898e9bcf4fb3bcce6c1409cc8edcf85a3965572456990d'
            '7d568c24f46902715c08797fc1148cfab9ee924d49c9bcd97cd1bd4106dfdd35409912ca1b598f50a50c62394f9618b595ca5bafdc4b9ee3b013398826cc4b01'
            '5e75c019e9fe8c67d686c4e3343dac1180a69a4bdb7d39b333415c63201eef9b98da5619dbf6fd8daa6884e65bc7f8afc9e52778682425e5a75987d527eae6f0')
b2sums=('f84598cc8ff4f38057c21271288d8c9b6106da3e5256d14191079272009b493e9ec51da80483e8767706ad4670b59e9f727285ea3c4c2a340f3230b9938492ea'
        '6fbc9f8128fb98cf5bc764a28da490241f329d276c47712cf9ac99afab2457e5b851c2e078f50f85e400a350675a38defb1f87a7b858a80efd017629659abf7b'
        '53cf2df2786f6bcbb3ca4c608b8d724690cae4f872ca4ac04f178e37904d57fd0dcf610141f5cf5a9c565d9a2b90a0fb240e42b29fdef0ae6edb24523dcb56e5'
        '8ae0bfdf6bc62460a64d84acb3dbd5d95257749f2560938eefd68a58727f310c8450ce756ed938ebe46a3074860d1abdd744689caf9bde01c89ae02f8c63179e'
        '987eeed26caf80e31ce289116f7d2fc7742949a6b5681005c0257a0fa490bb0bbbdde5ab1ec4794732bf58a22cabe9859c4c6a0f19b8be8aa97b5df659304657'
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
