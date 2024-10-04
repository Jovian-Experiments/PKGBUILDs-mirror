# Maintainer: Andreas Radke <andyrtr@archlinux.org>
# Maintainer: Robin Candau <antiz@archlinux.org>
# Contributor: Tom Gundersen <teg@jklm.no>
# Contributor: Andrea Scarpino <andrea@archlinux.org>
# Contributor: Geoffroy Carrier <geoffroy@archlinux.org>

pkgbase=bluez
pkgname=('bluez' 'bluez-utils' 'bluez-libs' 'bluez-cups' 'bluez-deprecated-tools' 'bluez-hid2hci' 'bluez-mesh')
pkgver=5.77
pkgrel=1.3
url="http://www.bluez.org/"
arch=('x86_64')
license=('GPL-2.0-only')
makedepends=('dbus' 'libical' 'systemd' 'alsa-lib' 'json-c' 'ell' 'python-docutils' 'python-pygments' 'cups' 'python>=3.11' 'python<3.12')
source=(https://www.kernel.org/pub/linux/bluetooth/${pkgname}-${pkgver}.tar.{xz,sign}
        bluetooth.modprobe
        0001-valve-bluetooth-config.patch  # SteamOS: Enable compatibility with devices like AirPods Pro
        0014-shared-gatt-Add-env-variable-to-prefer-indication-ov.patch # SteamOS: For Bluetooth qualification tests GAP/SEC/SEM/BV-56-C, GAP/SEC/SEM/BV-57-C and GAP/SEC/SEM/BV-58-C # not upstreamable
        0018-disable-unreliable-vcp-tests.patch
        0019-plugins-Add-new-plugin-to-manage-wake-policy.patch
        0020-plugins-wake-policy-Only-allow-Peripherals-to-wake-u.patch
        0021-valve-bluetooth-ll-privacy.patch

        # Holo: Fix for the Steam Controller that could block a suspend request
        # Part of https://gitlab.steamos.cloud/holo-team/tasks/-/issues/1267
        # At the moment of writing, the upstream patch has still not being merged
        # https://lore.kernel.org/all/CABBYNZKFEBuW2OeU4uOSfku=-jCnn3oXJENDMBGmkqP-4rybDA@mail.gmail.com/t/#u
        0001-BlueZ-adapter-Fix-execute-LE-Add-Device-To-Resolving.patch
        0002-Use-the-device-privacy-mode.patch
)
# see https://www.kernel.org/pub/linux/bluetooth/sha256sums.asc
sha256sums=('5d032fdc1d4a085813554f57591e2e1fb0ceb2b3616ee56f689bc00e1d150812'
            'SKIP'
            '46c021be659c9a1c4e55afd04df0c059af1f3d98a96338236412e449bf7477b4'
            '42ca8090a4b04854210c7b3a4618e5bb09457247993151549b4db2c9109dacc6'
            'a7928e6c78ce81abe9aa0022900a33577c1c76fd5bdf6e24f0c753013b8ead4c'
            'c0acf96d27bf2aec97cc1c1b66cc4be079712959d1ea266052f3e886d534c1e9'
            '120c7e435c854e4442e6de8dd257e19e142e2c36ebd491d18d7fa796f585f1ac'
            '0919781b35efb1e53b60dbad947ec282ad82f413879fd3e58af38a7b49a91941'
            '5800e6f6ff74a2a1b2c4482a393c65a83b10b0be52a53d51588e7a192d16fa0f'
            '24e49ec04e5c985d7f42acceb7c2dd9bad6ad6f8be80ff12368e18293448c42a'
            '170eef0d9b26a7e31ef2ce2039f662bf9558ee71a1f832538dc9ba5628659f69')
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
          --enable-datafiles \
          --enable-library --enable-deprecated # libraries and these tools are deprecated
  make

  # fake installation to be seperated into packages
  make DESTDIR="${srcdir}/fakeinstall" install

  # add missing tools FS#41132, FS#41687, FS#42716
  for files in `find tools/ -type f -perm -755`; do
    filename=$(basename $files)
    install -Dm755 "${srcdir}"/"${pkgbase}"-${pkgver}/tools/$filename "${srcdir}/fakeinstall"/usr/bin/$filename
  done
}

_install() {
  local src f dir
  for src; do
    f="${src#fakeinstall/}"
    dir="${pkgdir}/${f%/*}"
    install -m755 -d "${dir}"
    # use copy so a new file is created and fakeroot can track properties such as setuid
    cp -av "${src}" "${dir}/"
    rm -rf "${src}"
  done
}

check() {
  cd "$pkgname"-$pkgver
  # we (StamOS) have disabled a few tests broken by harness errors exposed
  # by -flto (the tests pass individually but not when run as a group)
  # upstream just does "make check || true" which is… an approach.
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
  depends=('systemd-libs' 'dbus' 'glib2' 'alsa-lib' 'glibc')
  backup=(etc/bluetooth/{main,input,network}.conf)

  _install fakeinstall/etc/bluetooth/main.conf
  _install fakeinstall/etc/bluetooth/input.conf
  _install fakeinstall/etc/bluetooth/network.conf
  _install fakeinstall/usr/lib/bluetooth/bluetoothd
  _install fakeinstall/usr/lib/systemd/system/bluetooth.service
  _install fakeinstall/usr/share/dbus-1/system-services/org.bluez.service
  _install fakeinstall/usr/share/dbus-1/system.d/bluetooth.conf
  _install fakeinstall/usr/share/man/man8/bluetoothd.8

  # bluetooth.service wants ConfigurationDirectoryMode=0555
  chmod -v 555 "${pkgdir}"/etc/bluetooth

  # add basic documention
  install -dm755 "${pkgdir}"/usr/share/doc/"${pkgbase}"/dbus-apis
  cp -a "${pkgbase}"-${pkgver}/doc/*.txt "${pkgdir}"/usr/share/doc/"${pkgbase}"/dbus-apis/
  # fix module loading errors
  install -dm755 "${pkgdir}"/usr/lib/modprobe.d
  install -Dm644 "${srcdir}"/bluetooth.modprobe "${pkgdir}"/usr/lib/modprobe.d/bluetooth-usb.conf
  # load module at system start required by some functions
  # https://bugzilla.kernel.org/show_bug.cgi?id=196621
  install -dm755 "$pkgdir"/usr/lib/modules-load.d
  echo "crypto_user" > "$pkgdir"/usr/lib/modules-load.d/bluez.conf

  # ship wake-policy config file
  install -Dm644 "${srcdir}"/"${pkgbase}"-${pkgver}/plugins/wake-policy.conf "${pkgdir}"/etc/bluetooth/wake-policy.conf
}

package_bluez-utils() {
  pkgdesc="Development and debugging utilities for the bluetooth protocol stack"
  depends=('dbus' 'systemd-libs' 'glib2' 'glibc' 'readline')
  optdepends=('ell: for btpclient')
  provides=('bluez-plugins')
  replaces=('bluez-plugins')

  _install fakeinstall/usr/bin/{advtest,amptest,avinfo,avtest,bcmfw,bdaddr,bluemoon,bluetoothctl,bluetooth-player,bneptest,btattach,btconfig,btgatt-client,btgatt-server,btinfo,btiotest,btmgmt,btmon,btpclient,btpclientctl,btproxy,btsnoop,check-selftest,cltest,create-image,eddystone,gatt-service,hcieventmask,hcisecfilter,hex2hcd,hid2hci,hwdb,ibeacon,isotest,l2ping,l2test,mcaptest,mpris-proxy,nokfw,oobtest,rctest,rtlfw,scotest,seq2bseq,test-runner}
  _install fakeinstall/usr/share/man/man1/bluetoothctl*.1
  _install fakeinstall/usr/share/man/man1/{btattach,btmgmt,btmon,isotest,l2ping,rctest}.1
  _install fakeinstall/usr/share/man/man5/org.bluez.{A,B,D,G,I,L,M,N,P}*.5
  _install fakeinstall/usr/share/man/man7/l2cap.7
  _install fakeinstall/usr/share/zsh/site-functions/_bluetoothctl
}

package_bluez-deprecated-tools() {
  pkgdesc="Deprecated tools that are no longer maintained"
  depends=('json-c' 'systemd-libs' 'glib2' 'dbus' 'readline' 'glibc')

  _install fakeinstall/usr/bin/{ciptool,hciattach,hciconfig,hcidump,hcitool,meshctl,rfcomm,sdptool}
  _install fakeinstall/usr/share/man/man1/{ciptool,hciattach,hciconfig,hcidump,hcitool,rfcomm,sdptool}.1
  _install fakeinstall/usr/share/man/man7/rfcomm.7
}

package_bluez-libs() {
  pkgdesc="Deprecated libraries for the bluetooth protocol stack"
  depends=('glibc')
  provides=('libbluetooth.so')
  license=('LGPL-2.1-only')

  _install fakeinstall/usr/include/bluetooth/*
  _install fakeinstall/usr/lib/libbluetooth.so*
  _install fakeinstall/usr/lib/pkgconfig/*
}

package_bluez-cups() {
  pkgdesc="CUPS printer backend for Bluetooth printers"
  depends=('cups' 'glib2' 'glibc' 'dbus')

  _install fakeinstall/usr/lib/cups/backend/bluetooth
}

package_bluez-hid2hci() {
  pkgdesc="Put HID proxying bluetooth HCI's into HCI mode"
  depends=('systemd-libs' 'glibc')

  _install fakeinstall/usr/lib/udev/*
  _install fakeinstall/usr/share/man/man1/hid2hci.1
}

package_bluez-mesh() {
  pkgdesc="Services for bluetooth mesh"
  depends=('json-c' 'readline' 'glibc')
  backup=('etc/bluetooth/mesh-main.conf')

  _install fakeinstall/etc/bluetooth/mesh-main.conf
  _install fakeinstall/usr/bin/{mesh-cfgclient,mesh-cfgtest}
  _install fakeinstall/usr/lib/bluetooth/bluetooth-meshd
  _install fakeinstall/usr/lib/systemd/system/bluetooth-mesh.service
  _install fakeinstall/usr/share/dbus-1/system-services/org.bluez.mesh.service
  _install fakeinstall/usr/share/dbus-1/system.d/bluetooth-mesh.conf
  _install fakeinstall/usr/share/man/man8/bluetooth-meshd.8

  # bluetooth.service wants ConfigurationDirectoryMode=0555
  chmod -v 555 "${pkgdir}"/etc/bluetooth
}
