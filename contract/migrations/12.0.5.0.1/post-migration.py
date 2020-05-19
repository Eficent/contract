def migrate(cr, version):
    cr.execute("""
        alter table res_company
        add column create_new_line_at_contract_line_renew boolean;
    """)
    cr.execute(
        """\
            UPDATE res_company
            SET create_new_line_at_contract_line_renew = true
        """
    )
