# Author : Clayton Craft <clayton@igalia.com>

pkgname='steamos-systemreport'
pkgver=0.5
pkgrel=1
pkgdesc='System report collection tool'
arch=('any')
license=('LGPL2.1')
url='https://gitlab.steamos.cloud/holo/holo'
source=(
  'steamos-systemreport'
  'steamos-systemreport-privileged'
  'org.valve.steamos.systemreport.policy'
)
sha256sums=(
  '23a3ae7d6da5e65fa139d77b7df09f752349267696b7e5172760865f16441144'
  '3840f44cc2c70506ba77f829bc3eb84fc8968924afa38d523ebd28467cbef70e'
  'b36473e3b77307450e75c59e248dde34d95b69c6c765a425fc30d9e201e23067'
)

package() {
  depends=(
    'bash'
    'rauc'                           # rauc status
    'drm_info'                       # drm_info
    'upower'                         # upower
    'wireplumber'                    # wpctl
    'iputils'                        # ping
    'iproute2'                       # ip
    'iwd'                            # iwctl
    'pciutils'                       # lspci
    'usbutils'                       # lsusb
    'systemd'                        # coredumpctl, journalctl
    'procps-ng'                      # ps
    'util-linux'                     # lsblk, hexdump
    'parted'                         # parted
    'smartmontools'                  # smartctl
    'steamos-customizations-jupiter' # steamos-{readonly,dump-info}
    'jupiter-hw-support'             # amd_system_info
    'polkit'
  )
  install -Dm755 steamos-systemreport -t "$pkgdir"/usr/bin/
  install -Dm755 steamos-systemreport-privileged -t "$pkgdir"/usr/bin/steamos-polkit-helpers
  install -m755 -d "$pkgdir"/usr/share/polkit-1/actions
  install -m644 org.valve.steamos.systemreport.policy -t "$pkgdir"/usr/share/polkit-1/actions
}
