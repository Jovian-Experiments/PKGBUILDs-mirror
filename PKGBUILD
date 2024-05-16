# Maintainer: Andreas Radke <andyrtr@archlinux.org>
# Maintainer: Robin Candau <antiz@archlinux.org>
# Contributor: Tom Gundersen <teg@jklm.no>
# Contributor: Andrea Scarpino <andrea@archlinux.org>
# Contributor: Geoffroy Carrier <geoffroy@archlinux.org>

pkgbase=bluez
pkgname=('bluez' 'bluez-utils' 'bluez-libs' 'bluez-cups' 'bluez-hid2hci' 'bluez-plugins')
pkgver=5.73
pkgrel=8
url="http://www.bluez.org/"
arch=('x86_64')
license=('GPL2')
makedepends=('dbus' 'libical' 'systemd' 'alsa-lib' 'json-c' 'python-docutils' 'python-pygments' 'cups')
source=(https://www.kernel.org/pub/linux/bluetooth/${pkgname}-${pkgver}.tar.{xz,sign}
        bluetooth.modprobe
        0001-valve-bluetooth-config.patch  # SteamOS: Enable compatibility with devices like AirPods Pro
        0002-valve-bluetooth-phy.patch     # SteamOS: Enable the phy # No longerneeded with kernel commit 288c90224eec55d13e786844b7954ef060752089, circa linux 6.4
        0014-shared-gatt-Add-env-variable-to-prefer-indication-ov.patch # SteamOS: For Bluetooth qualification tests GAP/SEC/SEM/BV-56-C, GAP/SEC/SEM/BV-57-C and GAP/SEC/SEM/BV-58-C # not upstreamable
        0017-device-Fix-airpods-pairing.patch
        0018-disable-unreliable-vcp-tests.patch
        0019-plugins-Add-new-plugin-to-manage-wake-policy.patch
        0020-plugins-wake-policy-Only-allow-Peripherals-to-wake-u.patch
        0021-valve-bluetooth-ll-privacy.patch
)
# see https://www.kernel.org/pub/linux/bluetooth/sha256sums.asc
sha256sums=('257e9075ce05c70d48c5defd254e78c418416f7584b45f9dddc884ff88e3fc53'
            'SKIP'
            '46c021be659c9a1c4e55afd04df0c059af1f3d98a96338236412e449bf7477b4'
            '42ca8090a4b04854210c7b3a4618e5bb09457247993151549b4db2c9109dacc6'
            '5d291d833c234a14b6162e3cb14eeff41505f5c3bb7c74528b65cb10597f39cb'
            'a7928e6c78ce81abe9aa0022900a33577c1c76fd5bdf6e24f0c753013b8ead4c'
            '7010fff3fadfabd298b0231576f4d820f5a1d39218540f4109a98eef6f2b29f2'
            'c0acf96d27bf2aec97cc1c1b66cc4be079712959d1ea266052f3e886d534c1e9'
            '120c7e435c854e4442e6de8dd257e19e142e2c36ebd491d18d7fa796f585f1ac'
            '0919781b35efb1e53b60dbad947ec282ad82f413879fd3e58af38a7b49a91941'
            '5800e6f6ff74a2a1b2c4482a393c65a83b10b0be52a53d51588e7a192d16fa0f'
            )
validpgpkeys=('E932D120BC2AEC444E558F0106CA9F5D1DCF2659') # Marcel Holtmann <marcel@holtmann.org>

build() {
  cd "${pkgname}"-${pkgver}

  # we patched a new plugin into Makefile.plugins so we need to re-run this:
  autoreconf -ivf

  ./configure \
          --prefix=/usr \
          --mandir=/usr/share/man \
          --sysconfdir=/etc \
          --localstatedir=/var \
          --libexecdir=/usr/lib \
          --with-dbusconfdir=/usr/share \
          --disable-obex \
          --enable-btpclient \
          --enable-midi \
          --enable-sixaxis \
          --enable-mesh \
          --enable-hid2hci \
          --enable-experimental \
          --enable-library # this is deprecated
  make
}

check() {
  cd "$pkgname"-$pkgver
  make check
}

prepare() {
  for patch in "${source[@]}"
  do
    case $patch in
      *.patch)
        echo "# Applying ${patch}"
        patch -d "${pkgname}"-${pkgver} -p1 -i "${srcdir}"/"${patch}"
        ;;
    esac
  done
}

package_bluez() {
  pkgdesc="Daemons for the bluetooth protocol stack"
  depends=('libical' 'dbus' 'glib2' 'alsa-lib' 'json-c' 'glibc')
  backup=('etc/bluetooth/main.conf')
  conflicts=('obexd-client' 'obexd-server')

  cd "${pkgbase}"-${pkgver}
  make DESTDIR=${pkgdir} \
       install-pkglibexecPROGRAMS \
       install-dbussessionbusDATA \
       install-systemdsystemunitDATA \
       install-systemduserunitDATA \
       install-dbussystembusDATA \
       install-dbusDATA \
       install-man8

  # ship upstream main config file
  install -dm555 "${pkgdir}"/etc/bluetooth
  install -Dm644 "${srcdir}"/"${pkgbase}"-${pkgver}/src/main.conf "${pkgdir}"/etc/bluetooth/main.conf

  # add basic documention
  install -dm755 "${pkgdir}"/usr/share/doc/"${pkgbase}"/dbus-apis
  cp -a doc/*.txt "${pkgdir}"/usr/share/doc/"${pkgbase}"/dbus-apis/
  # fix module loading errors
  install -dm755 "${pkgdir}"/usr/lib/modprobe.d
  install -Dm644 "${srcdir}"/bluetooth.modprobe "${pkgdir}"/usr/lib/modprobe.d/bluetooth-usb.conf
  # load module at system start required by some functions
  # https://bugzilla.kernel.org/show_bug.cgi?id=196621
  install -dm755 "$pkgdir"/usr/lib/modules-load.d
  echo "crypto_user" > "$pkgdir"/usr/lib/modules-load.d/bluez.conf

  # FS#74157 - bluez systemd service fails without localstatedir present
  install -dm700 "${pkgdir}"/var/lib/bluetooth

  # cleanup  - these libs go into bluez-libs
  rm "${pkgdir}"/usr/lib/libbluetooth.so*

  # ship wake-policy config file
  install -Dm644 "${srcdir}"/"${pkgbase}"-${pkgver}/plugins/wake-policy.conf "${pkgdir}"/etc/bluetooth/wake-policy.conf
}

package_bluez-utils() {
  pkgdesc="Development and debugging utilities for the bluetooth protocol stack"
  depends=('dbus' 'systemd' 'systemd-libs' 'glib2' 'glibc' 'readline')
  optdepends=('ell: for btpclient'
              'json-c: for mesh-cfgclient')
  backup=('etc/bluetooth/mesh-main.conf')
  conflicts=('bluez-hcidump')
  provides=('bluez-hcidump')
  replaces=('bluez-hcidump' 'bluez<=4.101')

  cd "${pkgbase}"-${pkgver}
  make DESTDIR="${pkgdir}" \
       install-binPROGRAMS \
       install-dist_zshcompletionDATA \
       install-man1

  # add missing tools FS#41132, FS#41687, FS#42716
  for files in `find tools/ -type f -perm -755`; do
    filename=$(basename $files)
    install -Dm755 "${srcdir}"/"${pkgbase}"-${pkgver}/tools/$filename "${pkgdir}"/usr/bin/$filename
  done
  
  # ship upstream mesh config file
  install -dm555 "${pkgdir}"/etc/bluetooth
  install -Dm644 "${srcdir}"/"${pkgbase}"-${pkgver}/mesh/mesh-main.conf "${pkgdir}"/etc/bluetooth/mesh-main.conf
 
  # libbluetooth.so* are part of libLTLIBRARIES and binPROGRAMS targets
  #make DESTDIR=${pkgdir} uninstall-libLTLIBRARIES
  #rmdir ${pkgdir}/usr/lib
  rm -rf "${pkgdir}"/usr/lib

  # move the hid2hci man page out
  mv "${pkgdir}"/usr/share/man/man1/hid2hci.1 "${srcdir}"/
}

package_bluez-libs() {
  pkgdesc="Deprecated libraries for the bluetooth protocol stack"
  depends=('glibc')
  provides=('libbluetooth.so')
  license=('LGPL2.1')

  cd "${pkgbase}"-${pkgver}
  make DESTDIR="${pkgdir}" \
       install-pkgincludeHEADERS \
       install-libLTLIBRARIES \
       install-pkgconfigDATA
}

package_bluez-cups() {
  pkgdesc="CUPS printer backend for Bluetooth printers"
  depends=('cups' 'glib2' 'glibc' 'dbus')

  cd "${pkgbase}"-${pkgver}
  make DESTDIR="${pkgdir}" install-cupsPROGRAMS

  # cleanup  - these libs go into bluez-libs
  rm "${pkgdir}"/usr/lib/libbluetooth.so*
}

package_bluez-hid2hci() {
  pkgdesc="Put HID proxying bluetooth HCI's into HCI mode"
  depends=('systemd' 'systemd-libs' 'glibc')

  cd "${pkgbase}"-${pkgver}
  make DESTDIR=${pkgdir} \
       install-udevPROGRAMS \
       install-rulesDATA
  
  install -dm755 "${pkgdir}"/usr/share/man/man1
  mv "${srcdir}"/hid2hci.1 "${pkgdir}"/usr/share/man/man1/hid2hci.1

  # cleanup  - these libs go into bluez-libs
  rm "${pkgdir}"/usr/lib/libbluetooth.so*
}

package_bluez-plugins() {
  pkgdesc="bluez plugins (PS3 Sixaxis controller)"
  depends=('systemd' 'systemd-libs' 'glibc')

  cd "${pkgbase}"-${pkgver}
  make DESTDIR="${pkgdir}" \
       install-pluginLTLIBRARIES

  # cleanup  - these libs go into bluez-libs
  rm "${pkgdir}"/usr/lib/libbluetooth.so*
}
